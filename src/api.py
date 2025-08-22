from fastapi import APIRouter, Depends, Request
from src.rest_models import UserCreate, User
from src.db_services import UserRepository


user_router = APIRouter()


# todo: Вынести в __init__.py пакета api
async def get_redis(request: Request):
    return request.app.state.redis


@user_router.post("/register", response_model=User)
async def register(user: UserCreate, repo: UserRepository = Depends()):
    return await repo.create_user(username=user.username)
