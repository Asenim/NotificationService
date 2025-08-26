from fastapi import APIRouter, Depends, Request, Response, HTTPException
from starlette import status

from src.shemas.rest_models import UserCreate, UserResponse, UserLogin
from src.shemas.security_models import SessionTokens
from src.db_services.user import UserRepository
from src.security import (
    create_session_tokens,
    generate_new_access_token_from_refresh
)


user_router = APIRouter()


@user_router.post("/register", response_model=UserResponse)
async def register(
        request: Request,
        response: Response,
        user: UserCreate,
        repo: UserRepository = Depends(),
):
    created_user = await repo.create_user(**user.model_dump())
    tokens = await create_session_tokens(
        request=request,
        response=response,
        user=created_user
    )
    return UserResponse(
        id=created_user.id,
        access_token=tokens.access,
        refresh_token=tokens.refresh
    )


@user_router.post("/login", response_model=SessionTokens)
async def login(
        request: Request,
        response: Response,
        user: UserLogin,
        repo: UserRepository = Depends(),
):
    received_user = await repo.get_user(**user.model_dump())
    tokens = await create_session_tokens(
        request=request,
        response=response,
        user=received_user
    )
    return SessionTokens(
        access=tokens.access,
        refresh=tokens.refresh,
    )


@user_router.post("/refresh", response_model=SessionTokens)
async def update_refresh_token(
        request: Request
):
    refresh = request.cookies.get("refresh_token")
    if not refresh:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing refresh token"
        )

    access = generate_new_access_token_from_refresh(refresh_token=refresh)

    return SessionTokens(
        access=access,
        refresh=refresh
    )
