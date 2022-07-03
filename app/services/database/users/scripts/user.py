from typing import Generator

from sqlalchemy import select

from app.models.telegram import User
from app.services.database.base import DB
from app.services.database.users.models import User as DBUser


class UsersDB(DB):

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
