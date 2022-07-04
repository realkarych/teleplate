from sqlalchemy import Column, BigInteger, String, DateTime, func

from app.services.database.base import Base


class User(Base):
    """Implements base table contains all registered in bot users"""

    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)  # Unique Telegram user id
    username = Column(String, default=None)
    user_fullname = Column(String, default=None)
    user_firstname = Column(String, default=None)
    registered_date = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"User: {self.user_id}, {self.username}, {self.user_firstname}, {self.user_fullname}, " \
               f"{self.registered_date}"

    def __str__(self) -> str:
        return f"User: {self.user_id}, {self.username}, {self.user_firstname}, {self.user_fullname}, " \
               f"{self.registered_date}"
