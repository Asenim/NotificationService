from fastapi import APIRouter, Depends, Request

from src.rest_models import UserCreate, User
from src.db_services import UserRepository
from src.security import create_access_token, create_refresh_token
from src.env import REFRESH_JWT_EXPIRE_MINUTES

user_router = APIRouter()


@user_router.post("/register", response_model=User)
async def register(
        request: Request,
        user: UserCreate,
        repo: UserRepository = Depends(),
):
    created_user = await repo.create_user(username=user.username)

    access = create_access_token(created_user.id)
    refresh = create_refresh_token(created_user.id)
    redis = request.app.state.redis
    expires_in = REFRESH_JWT_EXPIRE_MINUTES * 60
    await redis.set(
        f"refresh:{created_user.id}:{refresh['jti']}",
        refresh["token"], ex=expires_in)

    return User(
        id=created_user.id,
        access_token=access,
        refresh_token=refresh
    )
