# auth.py
from datetime import datetime, timedelta
from jose import jwt
from uuid import uuid4

from src.env import (
    JWT_SECRET, JWT_ALG,
    ACCESS_JWT_EXPIRE_MINUTES,
    REFRESH_JWT_EXPIRE_MINUTES,
)


def __create_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()

    # todo: Возможно будет лучше использовать int(datetime.now(timezone.utc))
    iat = datetime.utcnow()
    exp = datetime.utcnow() + expires_delta
    jti = str(uuid4())
    to_encode.update({"exp": exp, "iat": iat, "jti": jti})

    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALG)

    # todo: Возможно лучше будет сюда тоже прикрутить pydantic или хотя бы dataclass
    return {"token": token, "jti": jti, "exp": exp, "iat": iat}


def create_access_token(user_id: int):
    return __create_token(
        {"sub": str(user_id), "type": "access"},
        timedelta(minutes=ACCESS_JWT_EXPIRE_MINUTES),
    )


def create_refresh_token(user_id: int):
    return __create_token(
        {"sub": str(user_id), "type": "refresh"},
        timedelta(minutes=REFRESH_JWT_EXPIRE_MINUTES),
    )
