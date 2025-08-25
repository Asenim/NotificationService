from pydantic import BaseModel

from src.enums import NotificationType


class UserCreate(BaseModel):
    username: str


class User(BaseModel):
    id: int
    access_token: str
    refresh_token: str


class UserLogin(BaseModel):
    username: str


class NotificationCreate(BaseModel):
    type: NotificationType
    text: str
