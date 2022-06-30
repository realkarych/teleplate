from aiogram import types, Dispatcher

from bot.core.navigation.nav import Commands


async def cmd_start(message: types.Message):
    await message.answer("Hello from Teleplate!")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=str(Commands.start))
