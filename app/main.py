from fastapi import FastAPI, Depends, HTTPException
from app.core.config import get_settings

from app.models.user import User

from app.db.base import Base
from app.db.session import engine, get_db

from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from sqlalchemy.exc import IntegrityError



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


@app.post("/users", response_model = UserResponse, status_code=201)
def create_user(user:UserCreate, db:Session = Depends(get_db)): 
    db_user = User(email = user.email)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=404, detail= "Email already exists")

    return db_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users



@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    
    return user



@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail= "User not found")
    
    if user.email is not None:
        db_user.email = user.email
    
    db.commit()
    db.refresh(db_user)
    
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail= "User not found")

    return {"message":"User deleted"}


# Creates physical db table
Base.metadata.create_all(bind=engine) 

