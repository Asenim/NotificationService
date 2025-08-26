from fastapi import APIRouter, Depends, Request, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.shemas.rest_models import NotificationCreate, Notification
from src.security import decode_access_token
from src.db_services.notifications import NotificationRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
notification_router = APIRouter()


@notification_router.get("/notifications")
def get_notifications(token: str = Depends(oauth2_scheme)):
    return token


@notification_router.post("/notifications", response_model=Notification)
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

    return Notification(
        user_id=notification_data.user.id,
        type=notification_data.type,
        text=notification_data.text
    )
