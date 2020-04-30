from fastapi_users import models
from fastapi_users.db import TortoiseUserDatabase, TortoiseBaseUserModel
from tortoise import fields
from tortoise.models import Model


class User(models.BaseUser):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserModel(TortoiseBaseUserModel):
    pass


class FileLinks(Model):
    """ Таблица ссылок пользователей """

    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserModel', related_name='files_links')
    link = fields.CharField(max_length=500, index=True)


user_db = TortoiseUserDatabase(UserDB, UserModel)
