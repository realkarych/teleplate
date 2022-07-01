import asyncio
import types

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.bot_command_scope import BotCommandScopeDefault
from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.settings.app import AppSettings
from bot.config import load_config
from bot.core.handlers import new_user
from bot.core.middlewares.throttling import ThrottlingMiddleware
from bot.core.navigation.nav import Commands
from bot.core.updates_worker import get_handled_updates_list
from bot.services.database.base import Base
from bot.services.schedule.scheduler import Scheduler


class HandlersFactory:

    def __init__(self, dp: Dispatcher) -> None:
        self._dp = dp

    def register(self, *handlers) -> None:
        """Handlers registering. If `register_handlers()` wasn't implemented in handlers' module -> skipping module
            with error message"""

        for handler in handlers:

            if isinstance(handler, types.ModuleType):
                try:
                    handler.register_handlers(self._dp)
                except AttributeError as error:
                    logger.error(f"register_handlers() method wasn't implemented in {str(error.obj)}")

            else:
                logger.error(f"{handler} from submitted args to `register_handlers()` is not a .py module")


async def __set_bot_commands(bot: Bot) -> None:
    """Create a commands' list (shortcuts) in Telegram bot menu"""

    commands = [command().to_bot_command() for command in Commands]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


def __register_schedulers() -> None:
    """Init schedulers by APScheduler singleton instance"""


async def main() -> None:
    """Method that starts app & polling"""

    logger.add("bot.log", rotation="500 MB")

    config: AppSettings = load_config()

    engine = create_async_engine(
        config.postgresql_uri,
        future=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_sessionmaker = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    storage = MemoryStorage()
    bot = Bot(config.bot.token, parse_mode="HTML")

    # Providing db session-maker to handlers via bot instance.
    # In handler: `session = m.bot.get("db")`
    bot["db"] = async_sessionmaker

    dp = Dispatcher(bot, storage=storage)

    Scheduler()
    __register_schedulers()
    await __set_bot_commands(bot)

    # Provide your handler-modules into `register(...)`
    HandlersFactory(dp).register(new_user, )

    # Setup all your middlewares here
    dp.middleware.setup(ThrottlingMiddleware())

    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    """Log this is pointless"""

except Exception as e:
    logger.critical(str(e))
