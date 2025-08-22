from tortoise.contrib.fastapi import register_tortoise

from src.env import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    DB_HOST, DB_PORT
)


def init_db(app):
    register_tortoise(
        app=app,
        db_url=f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}",
        modules={"models": ["src.models"]},
        generate_schemas=True,
    )
