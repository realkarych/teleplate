from aiogram import types, Dispatcher

from bot.core.navigation.nav import Commands
from bot.misc import messages as msgs
from bot.models.telegram import User
from bot.services.database.users.scripts.user import UsersDB


async def cmd_start(m: types.Message):
    user = User(user=m.from_user)

    session = UsersDB(db_session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.welcome(user_firsname=user.firstname))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=str(Commands.start))
