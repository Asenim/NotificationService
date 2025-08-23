import os

from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB: str = os.getenv("POSTGRES_DB")
DB_HOST: str = os.getenv("DB_HOST")
DB_PORT: str = os.getenv("DB_PORT")

REDIS_HOST: str = os.getenv("REDIS_HOST")
REDIS_PORT: str = os.getenv("REDIS_PORT")

AVATAR_URL: str = os.getenv("AVATAR_URL")

JWT_SECRET: str = os.getenv("JWT_SECRET")
JWT_ALG: str = os.getenv("JWT_ALG")
ACCESS_JWT_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_JWT_EXPIRE_MINUTES"))
REFRESH_JWT_EXPIRE_MINUTES: int = int(os.getenv("REFRESH_JWT_EXPIRE_MINUTES"))
