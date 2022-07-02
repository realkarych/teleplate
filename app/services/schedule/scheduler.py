import tzlocal
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.models.types import Singleton


class Scheduler(metaclass=Singleton):
    __scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))

    def __init__(self):
        self.__scheduler.start()

    def get(self) -> AsyncIOScheduler:
        return self.__scheduler
