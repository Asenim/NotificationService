import redis
from tortoise.contrib.fastapi import register_tortoise

from src.env import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    DB_HOST, DB_PORT,
    REDIS_HOST, REDIS_PORT
)


async def init_redis():
    return redis.asyncio.from_url(
        f"redis://{REDIS_HOST}:{REDIS_PORT}",
        decode_responses=True
    )


def init_db(app):
    register_tortoise(
        app=app,
        db_url=f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}",
        modules={"models": ["src.models"]},
        generate_schemas=True,
    )
