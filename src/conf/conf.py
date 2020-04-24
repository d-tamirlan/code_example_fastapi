from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication, CookieAuthentication
from fastapi_users import models
from starlette.templating import Jinja2Templates

from src.models import user_db, UserDB, User


SECRET_KEY = "^-r+qb5+fs7c#7%7j7_6)tvf%nnd4a41_2jm3gg9zp4v%x+h-@"
templates = Jinja2Templates(directory="src/templates")

auth_backends = [
    JWTAuthentication(secret=SECRET_KEY, lifetime_seconds=6000),
    CookieAuthentication(secret=SECRET_KEY, lifetime_seconds=6000),
]


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    models.BaseUserCreate,
    models.BaseUserUpdate,
    UserDB,
    SECRET_KEY
)
