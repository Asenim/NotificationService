from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.models import Notification
from src.enums import NotificationType
from src.db_services.user import UserRepository


class NotificationRepository:
    @staticmethod
    async def get_notifications(
            user_id: int,
            limit: int,
            offset: int
    ):
        user = await UserRepository.get_user(user_id=user_id)
        notifications = (
            await Notification.filter(user_id=user.id)
            .order_by("-created_at")
            .offset(offset)
            .limit(limit)
        )

        return user, notifications

    @staticmethod
    async def create_notification(
            user_id: int,
            notification_type: NotificationType,
            text: str
    ) -> Notification:

        # user = await UserRepository.get_user(user_id=user_id)
        notification = await Notification.create(
            user_id=user_id,    # user=user.id
            type=notification_type,
            text=text
        )

        # await notification.fetch_related("user")
        return notification

    @staticmethod
    async def delete_notification(
            notification_id: int,
            user_id: int
    ) -> None:
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
