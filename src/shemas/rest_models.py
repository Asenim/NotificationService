from pydantic import BaseModel, ConfigDict

from src.enums import NotificationType


class UserCreate(BaseModel):
    username: str


class User(BaseModel):
    id: int
    access_token: str
    refresh_token: str


class UserLogin(BaseModel):
    username: str


class Notification(BaseModel):
    user_id: int
    type: NotificationType
    text: str

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
    )


class NotificationCreate(BaseModel):
    notification_type: NotificationType
    text: str

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
    )


class NotificationDeleted(BaseModel):
    user_id: int
    notification_id: int
    detail: str
