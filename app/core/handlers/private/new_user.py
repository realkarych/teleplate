from aiogram import types, Dispatcher
from aiogram.types import ChatType

from app.core.middlewares.throttling import throttle
from app.core.navigation.nav import Commands
from app.messages import new_user as msgs
from app.models.telegram import User
from app.services.database.users.scripts.user import UsersDB


@throttle(limit=2)
async def cmd_start(m: types.Message):
    user = User(user=m.from_user)

    session = UsersDB(db_session=m.bot.get("db"))
    await session.add_user(user)

    await m.answer(msgs.welcome(user_firsname=user.firstname), reply_markup=None)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=str(Commands.start), chat_type=ChatType.PRIVATE)
