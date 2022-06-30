from aiogram import types, Dispatcher

from bot.core.navigation.nav import Commands
from bot.models.telegram import User
from bot.services.database.users.scripts.user import UsersDB


async def cmd_start(m: types.Message):
    user = User(message=m)

    session = UsersDB(db_session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer("Hello from Teleplate!")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=str(Commands.start))
