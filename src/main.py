import uvicorn

from fastapi import FastAPI
from src.db import init_db, init_redis
from src.api import user, notifications


app = FastAPI()

init_db(app=app)


@app.on_event("startup")
async def startup_event():
    app.state.redis = await init_redis()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()


app.include_router(user.user_router, prefix="/auth")
app.include_router(notifications.notification_router)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8080
    )
