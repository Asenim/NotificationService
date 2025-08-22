from datetime import datetime
from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    avatar_url = fields.CharField(max_length=250)
    created_at = fields.DateField(default=datetime.today)
