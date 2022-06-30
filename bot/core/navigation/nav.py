from dataclasses import dataclass
from enum import Enum, unique

from aiogram.types import BotCommand, InlineKeyboardButton


@dataclass
class Command:
    name: str
    description: str

    def to_bot_command(self) -> BotCommand:
        """Map Command object to BotCommand object"""

        return BotCommand(command=self.name, description=self.description)


@unique
class Commands(Enum):
    """List of commands with public access. Do not implement here admin commands & specific commands (will be submitted
    to Telegram menu list.)"""

    start = Command(name='start', description='Start Bot')

    def __str__(self) -> str:
        return self.value.name

    def __repr__(self) -> str:
        return self.value.name

    def __call__(self, *args, **kwargs) -> Command:
        return self.value


class ReplyCallbacks(Enum):
    """List of reply text buttons."""

    example = "Some reply button"

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


@dataclass
class InlineCallback:
    text: str
    callback: str

    def to_inline_button(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=self.text, callback_data=self.callback)


@unique
class InlineCallbacks(Enum):
    """Store inline buttons here"""

    some_button = InlineCallback(text="Displaying Text", callback='some_callback')
