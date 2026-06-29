import os
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = urllib.parse.quote_plus(os.getenv("DB_PASSWORD"))
server = os.getenv("DB_SERVER")
instance = os.getenv("DB_INSTANCE")
db_name = os.getenv("DB_NAME")

if instance and instance.upper() != "MSSQLSERVER":
    host = f"{server}\\{instance}"
else:
    host = server

DATABASE_URL = f"mssql+pymssql://{user}:{password}@{host}/{db_name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
