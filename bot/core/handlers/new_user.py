from aiogram import types, Dispatcher


async def cmd_start(message: types.Message):
    await message.answer("Привет, на связи Teleplate!")


def register_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
