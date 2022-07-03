import tzlocal
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.models.types import Singleton


class Scheduler(metaclass=Singleton):
    _scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))

    def __init__(self):
        self._scheduler.start()

    def get(self) -> AsyncIOScheduler:
        return self._scheduler
