from fastapi import FastAPI
from routers import router
from conf.conf import fastapi_users
from conf.database import database

app = FastAPI()


app.include_router(fastapi_users.router, prefix="/api/users", tags=["users"])
app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
