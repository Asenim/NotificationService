from fastapi import APIRouter, Depends, Request
from src.rest_models import UserCreate, User
from src.db_services import UserRepository


user_router = APIRouter()


@user_router.post("/register", response_model=User)
async def register(user: UserCreate, repo: UserRepository = Depends()):
    created_user = await repo.create_user(username=user.username)
    # todo: Тут будет вызов создание JWT токена

    return User(
        id=created_user.id,
        access_token="none",
        refresh_token="none"
    )

