import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import databases


DATABASE_URL = "postgresql://postgres:asHvgnoI02S3oEc@db/project_db"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = Session()

Base: DeclarativeMeta = declarative_base()
