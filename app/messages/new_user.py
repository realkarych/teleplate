from aiogram.utils.markdown import hbold as bold, hlink as link


def welcome(user_firsname: str) -> str:
    return bold(f'Hello, {user_firsname}!') + \
           f"\n\nThis is {link(title='Teleplate', url='https://github.com/devkarych/teleplate')}" \
           f".\nAuthor: @karych."
