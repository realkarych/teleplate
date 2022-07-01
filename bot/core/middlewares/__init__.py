from aiogram import Dispatcher

from bot.core.middlewares.throttling import ThrottlingMiddleware


def setup(dispatcher: Dispatcher):
    """Setup middlewares with given dispatcher"""
    dispatcher.setup_middleware(ThrottlingMiddleware)