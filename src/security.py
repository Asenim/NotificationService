from fastapi import Request
from datetime import datetime, timedelta
from jose import jwt
from uuid import uuid4

from src.env import (
    JWT_SECRET, JWT_ALG,
    ACCESS_JWT_EXPIRE_MINUTES,
    REFRESH_JWT_EXPIRE_MINUTES,
)
from src.models import User
from src.security_models import SessionTokens, Token


def __create_token(data: dict, expires_delta: timedelta) -> Token:
    to_encode = data.copy()

    # todo: Возможно будет лучше использовать int(datetime.now(timezone.utc))
    iat = datetime.utcnow()
    exp = datetime.utcnow() + expires_delta
    jti = str(uuid4())
    to_encode.update({"exp": exp, "iat": iat, "jti": jti})

    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALG)

    return Token(
        token=token,
        jti=jti,
        iat=iat,
        exp=exp
    )


def create_access_token(user_id: int) -> Token:
    return __create_token(
        {"sub": str(user_id), "type": "access"},
        timedelta(minutes=ACCESS_JWT_EXPIRE_MINUTES),
    )


def create_refresh_token(user_id: int) -> Token:
    return __create_token(
        {"sub": str(user_id), "type": "refresh"},
        timedelta(minutes=REFRESH_JWT_EXPIRE_MINUTES),
    )


def create_session_tokens(request: Request, user: User) -> SessionTokens:
    access = create_access_token(user.id)
    refresh = create_refresh_token(user.id)
    redis = request.app.state.redis
    expires_in = REFRESH_JWT_EXPIRE_MINUTES * 60
    await redis.set(
        f"refresh:{user.id}:{refresh.jti}",
        refresh.token, ex=expires_in)

    return SessionTokens(
        access=access,
        refresh=refresh
    )
