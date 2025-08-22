from src.models import User
from src.env import AVATAR_URL


class UserRepository:
    @staticmethod
    async def create_user(username):
        return await User.create(
            username=username,
            avatar_url=AVATAR_URL,
        )
