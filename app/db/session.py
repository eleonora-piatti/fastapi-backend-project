from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import get_settings

settings = get_settings()

DB_URL = "sqlite:///./app.db"

engine = create_engine(
    DB_URL,
    connect_args={
        "check_same_thread":False
    }
)

SessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush=False
)


# dependency db for fastAPI

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



