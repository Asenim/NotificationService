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
                status_code=409,
                detail="User with this username already exists"
            )

    @staticmethod
    async def get_user(username: str) -> User:
        try:
            user = await User.get(username=username)
            return user
        except DoesNotExist:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
