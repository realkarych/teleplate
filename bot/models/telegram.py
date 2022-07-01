from dataclasses import dataclass

from aiogram import types


@dataclass
class User:
    def __init__(self, user: types.User):
        self.id: int = user.id
        self.fullname: str = user.full_name
        self.firstname: str = user.first_name
        self.username: str = user.username
