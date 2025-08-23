# auth.py
from datetime import datetime, timedelta
from jose import jwt

from src.env import (
    JWT_SECRET, JWT_ALG,
    ACCESS_JWT_EXPIRE_MINUTES,
    REFRESH_JWT_EXPIRE_MINUTES,
)


def create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALG)


def create_access_token(user_id: int):
    return create_token(
        {"sub": str(user_id), "type": "access"},
        timedelta(minutes=ACCESS_JWT_EXPIRE_MINUTES),
    )


def create_refresh_token(user_id: int):
    return create_token(
        {"sub": str(user_id), "type": "refresh"},
        timedelta(minutes=REFRESH_JWT_EXPIRE_MINUTES),
    )
