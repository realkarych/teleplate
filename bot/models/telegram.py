from dataclasses import dataclass
from typing import Union

from aiogram import types


@dataclass
class User:
    def __init__(self, message: Union[types.Message, types.CallbackQuery]):
        self.id: int = message.from_user.id
        self.fullname: str = message.from_user.full_name
        self.firstname: str = message.from_user.first_name
        self.username: str = message.from_user.username
