from enum import Enum


class NotificationType(str, Enum):
    LIKE = "like"
    COMMENT = "comment"
    REPOST = "repost"
