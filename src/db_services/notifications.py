from src.models import Notification
from src.enums import NotificationType


class NotificationRepository:
    @staticmethod
    async def create_notification(
            user_id: int,
            notification_type: NotificationType,
            text: str
    ) -> Notification:
        notification = await Notification.create(
            user_id=user_id,
            type=notification_type,
            text=text
        )
        return notification
