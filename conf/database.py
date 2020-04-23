import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import databases


DATABASE_URL = "sqlite:///./test.db"
database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()

Base: DeclarativeMeta = declarative_base()
