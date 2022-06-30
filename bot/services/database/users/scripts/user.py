from typing import Generator

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from bot.models.telegram import User
from bot.services.database.users.models import User as DBUser


class UsersDB:

    def __init__(self, db_session: sessionmaker):
        self._session: sessionmaker = db_session
        pass

    async def add_user(self, user: User) -> None:
        """Add new user to database"""

        async with self._session() as session:
            await session.merge(DBUser(user_id=user.id, username=user.username, user_fullname=user.fullname,
                                       user_firstname=user.firstname))
            await session.commit()

    async def get_all_users(self) -> Generator[DBUser, None, None]:
        """Returns generator obj of all registered in bot users"""

        async with self._session() as session:
            all_users_request = await session.execute(select(DBUser))
            users = all_users_request.scalars()
            for user in users:
                yield user
