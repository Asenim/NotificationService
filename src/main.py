import uvicorn

from fastapi import FastAPI
from src.db import init_db


app = FastAPI()

init_db(app=app)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080
    )
