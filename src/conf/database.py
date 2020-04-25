import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import databases
from envparse import env


env.read_envfile()

POSTGRES_USER = env('POSTGRES_USER', None)
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', None)
POSTGRES_HOST = env('POSTGRES_HOST', None)
POSTGRES_DB = env('POSTGRES_DB', None)

DATABASE_URL = env('DATABASE_URL', None)

if not DATABASE_URL:
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()

Base: DeclarativeMeta = declarative_base()
