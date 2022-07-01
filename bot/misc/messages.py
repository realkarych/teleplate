from aiogram.utils.markdown import hbold, hlink


def welcome(user_firsname: str) -> str:
    return hbold(f'Hello, {user_firsname}!') + \
           f"\n\nThis is {hlink(title='Teleplate', url='https://github.com/devkarych/teleplate')}.\nAuthor: @karych."
