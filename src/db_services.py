from src.models import User
from src.env import AVATAR_URL


class UserRepository:
    @staticmethod
    async def create_user(username):
        # todo: Сделать обработку исключения когда создается пользователь с существующим username
        return await User.create(
            username=username,
            avatar_url=AVATAR_URL,
        )

    @staticmethod
    async def get_user(username):
        return await User.get(username=username)
