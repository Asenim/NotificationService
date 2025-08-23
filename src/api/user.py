from fastapi import APIRouter, Depends, Request

from src.rest_models import UserCreate, User
from src.db_services import UserRepository
from src.security import create_session_tokens


user_router = APIRouter()


@user_router.post("/register", response_model=User)
async def register(
        request: Request,
        user: UserCreate,
        repo: UserRepository = Depends(),
):
    created_user = await repo.create_user(username=user.username)
    tokens = create_session_tokens(request=request, user=created_user)
    return User(
        id=created_user.id,
        access_token=tokens.access,
        refresh_token=tokens.refresh
    )
