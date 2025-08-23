from datetime import datetime

from pydantic import BaseModel


class SessionTokens(BaseModel):
    access: str
    refresh: str


class Token(BaseModel):
    token: str
    jti: str
    iat: datetime
    exp: datetime

