from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str


class User(BaseModel):
    id: int
    access_token: str
    refresh_token: str
