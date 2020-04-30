from fastapi import FastAPI
from src.routers import router
from src.conf.conf import fastapi_users
from src.conf.database import DB_CONFIG
from tortoise.contrib.starlette import register_tortoise


app = FastAPI()


app.include_router(fastapi_users.router, prefix="/api/users", tags=["users"])
app.include_router(router)

register_tortoise(app, config=DB_CONFIG, generate_schemas=True)
