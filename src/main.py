import uvicorn

from fastapi import FastAPI
from src.db import init_db
from api import router

app = FastAPI()

init_db(app=app)

app.include_router(router, prefix="/auth")


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080
    )
