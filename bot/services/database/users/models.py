from sqlalchemy import Column, BigInteger, String

from bot.services.database.base import Base
from bot.services.date_manager import get_current_date


class User(Base):
    """Implements base table contains all registered in bot users"""

    __tablename__ = "tbl_users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String, default=None)
    user_fullname = Column(String, default=None)
    user_firstname = Column(String, default=None)
    registered_date = Column(String, default=get_current_date)

    def __repr__(self) -> str:
        return f"User: {self.user_id}, {self.username}, {self.user_firstname}, {self.user_fullname}, " \
               f"{self.registered_date}"

    def __str__(self) -> str:
        return f"User: {self.user_id}, {self.username}, {self.user_firstname}, {self.user_fullname}, " \
               f"{self.registered_date}"
