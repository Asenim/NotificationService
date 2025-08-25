from starlette import status
from tortoise.exceptions import DoesNotExist, IntegrityError
from fastapi import HTTPException

from src.models import User
from src.env import AVATAR_URL


class UserRepository:
    @staticmethod
    async def create_user(username: str) -> User:
        try:
            user = await User.create(
                username=username,
                avatar_url=AVATAR_URL,
            )
            return user
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this username already exists"
            )

    @staticmethod
    async def get_user(username: str) -> User:
        try:
            user = await User.get(username=username)
            return user
        except DoesNotExist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
