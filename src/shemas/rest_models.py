from pydantic import BaseModel, Field

from src.shemas import ConfigModel
from src.enums import NotificationType


class UserCreate(BaseModel):
    username: str


class UserResponse(BaseModel):
    id: int
    access_token: str
    refresh_token: str


class UserLogin(BaseModel):
    username: str


class NotificationCreatedResponse(ConfigModel):
    user_id: int
    type: NotificationType
    text: str


class NotificationCreate(ConfigModel):
    notification_type: NotificationType = Field(alias="type")
    text: str


class NotificationDeleted(BaseModel):
    user_id: int
    notification_id: int
    detail: str


class NotificationsResponse(ConfigModel):
    user: str
    notifications: list[NotificationCreate]
