import asyncio
import types

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.bot_command_scope import BotCommandScopeDefault
from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import load_config
from app.core import middlewares
from app.core.handlers.private import new_user
from app.core.navigation.nav import Commands
from app.core.updates_worker import get_handled_updates_list
from app.services.database.base import Base
from app.services.schedule.scheduler import Scheduler
from app.settings.app import AppSettings
from app.settings.base import AppEnvTypes


class HandlersFactory:

    def __init__(self, dp: Dispatcher) -> None:
        self._dp = dp

    def register(self, *handlers) -> None:
        """Handlers registering. If `register_handlers()` wasn't implemented in
        handlers' module -> skipping module with error message"""

        for handler in handlers:

            if isinstance(handler, types.ModuleType):
                try:
                    handler.register_handlers(self._dp)
                except AttributeError as error:
                    logger.error(f"register_handlers() method wasn't implemented "
                                 f"in {str(error.obj)}")

            else:
                logger.error(f"{handler} from submitted args to `register_handlers()` "
                             f"is not a .py module")


async def _set_bot_commands(bot: Bot) -> None:
    """Create a commands' list (shortcuts) in Telegram app menu"""

    commands = [command().to_bot_command() for command in Commands]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


def _register_schedulers() -> None:
    """Init schedulers by APScheduler singleton instance"""


async def main() -> None:
    """Method that starts app & polling"""

    logger.add("app.log", rotation="500 MB")

    config: AppSettings = load_config(app_type=AppEnvTypes.DEV)

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
    bot = Bot(config.token, parse_mode=config.parse_mode)

    # Providing db session-maker to handlers via bot instance.
    # In handler: `session = m.bot.get("db")`
    bot["db"] = async_sessionmaker

    dp = Dispatcher(bot, storage=storage)

    Scheduler()
    _register_schedulers()
    await _set_bot_commands(bot)

    # Provide your handler-modules into `register(...) func`
    HandlersFactory(dp).register(new_user, )

    middlewares.setup(dp)

    try:
        await dp.start_polling(allowed_updates=get_handled_updates_list(dp))
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    # Log this is pointless
    pass
