from datetime import datetime
from tortoise import fields
from tortoise.models import Model

from src.enums import NotificationType


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    avatar_url = fields.CharField(max_length=250)
    created_at = fields.DateField(default=datetime.today)


class Notification(Model):
    id = fields.IntField(pk=True)
    user_id: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="notifications", on_delete=fields.CASCADE
    )
    type = fields.CharEnumField(NotificationType, max_length=20)
    text = fields.TextField()
    created_at = fields.DatetimeField(default=datetime.today)
