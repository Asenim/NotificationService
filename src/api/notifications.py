from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.shemas.rest_models import (
    NotificationCreate,
    NotificationCreatedResponse,
    NotificationDeleted,
    NotificationsResponse,
)
from src.security import decode_access_token
from src.db_services.notifications import NotificationRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
notification_router = APIRouter()


@notification_router.get("/notifications", response_model=NotificationsResponse)
async def get_notifications(
        limit: int = 10,
        offset: int = 10,
        repo: NotificationRepository = Depends(),
        token: str = Depends(oauth2_scheme)
):
    payload = decode_access_token(token=token)
    user, notifications = await repo.get_notifications(
        user_id=int(payload.get("sub")),
        limit=limit,
        offset=offset
    )

    return NotificationsResponse(
        user=f"{user.username} {user.avatar_url}",
        notifications=notifications
    )


@notification_router.post(
    "/notifications",
    response_model=NotificationCreatedResponse
)
async def create_notifications(
        data: NotificationCreate,
        repo: NotificationRepository = Depends(),
        token: str = Depends(oauth2_scheme),
):
    payload = decode_access_token(token=token)
    user_id = int(payload.get("sub"))

    notification_data = await repo.create_notification(
        user_id=user_id,
        **data.model_dump()
    )

    return NotificationCreatedResponse(
        user_id=user_id,    # notification_data.user.id,
        type=notification_data.type,
        text=notification_data.text
    )


@notification_router.delete(
    "/notifications/{notification_id}",
    response_model=NotificationDeleted)
async def delete_notifications(
        notification_id: int,
        repo: NotificationRepository = Depends(),
        token: str = Depends(oauth2_scheme),
):
    payload = decode_access_token(token=token)
    user_id = int(payload.get("sub"))
    await repo.delete_notification(
        user_id=user_id,
        notification_id=notification_id
    )
    return NotificationDeleted(
        user_id=user_id,
        notification_id=notification_id,
        detail="Notification deleted"
    )
