from sqlalchemy import Column, BigInteger, String

from bot.services.database.base import Base


class Users(Base):
    """Implements base table contains all registered users"""

    __tablename__ = "tbl_users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String, default=None)
