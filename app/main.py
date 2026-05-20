from fastapi import FastAPI, Depends
from app.core.config import get_settings

from app.models.user import User

from app.db.base import Base
from app.db.session import engine, get_db

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate


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


@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return {"error":"User not found"}
    
    if user.email is not None:
        db_user.email = user.email
    
    db.commit()
    db.refresh(db_user)
    
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return {"error":"User not found"}

    return {"message":"User deleted"}


# Creates physical db table
Base.metadata.create_all(bind=engine) 

