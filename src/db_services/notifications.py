from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.models import Notification
from src.enums import NotificationType
from src.db_services.user import UserRepository


class NotificationRepository:
    @staticmethod
    async def create_notification(
            user_id: int,
            notification_type: NotificationType,
            text: str
    ) -> Notification:

        user = await UserRepository.get_user(user_id=user_id)
        notification = await Notification.create(
            user=user,
            type=notification_type,
            text=text
        )

        await notification.fetch_related("user")
        return notification

    @staticmethod
    async def delete_notification(notification_id: int, user_id: int):
        try:
            notification = await Notification.get(id=notification_id)
            await notification.fetch_related("user")
        except DoesNotExist:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )
        if notification.user.id != user_id:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to delete this notification"
            )

        await notification.delete()
