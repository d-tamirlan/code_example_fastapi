from fastapi_users import models
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, ForeignKey, Integer

from src.conf.database import Base, database, engine


class User(models.BaseUser):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


class FileLinks(Base):
    """ Таблица ссылок пользователей """

    __tablename__ = "files_links"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("user.id", ondelete="cascade"), nullable=False)
    link = Column(String, index=True, nullable=False)

    def __init__(self, user_id, link):
        self.user_id = user_id
        self.link = link


Base.metadata.create_all(engine)

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

