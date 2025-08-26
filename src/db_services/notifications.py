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
        print(user, type(user))
        notification = await Notification.create(
            user=user,
            type=notification_type,
            text=text
        )

        await notification.fetch_related("user")
        return notification
