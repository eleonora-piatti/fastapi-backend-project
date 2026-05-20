from fastapi import FastAPI, Depends
from app.core.config import get_settings

from app.models.user import User

from app.db.base import Base
from app.db.session import engine, get_db

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate


settings = get_settings()

app = FastAPI(
    title = settings.app_name,
    debug = settings.debug
)


@app.get("/health")
def health():
    return {
        "status" : "ok",
        "environment" : settings.environment  
        }


@app.post("/users")
def create_user(user:UserCreate, db:Session = Depends(get_db)): 
    db_user = User(email = user.email)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return user



@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


# Creates physical db table
Base.metadata.create_all(bind=engine) 

