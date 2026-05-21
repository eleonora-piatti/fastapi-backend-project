from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])



@router.post("", response_model = UserResponse, status_code=201)
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


@router.get("")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    
    return user


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail= "User not found")
    
    if user.email is not None:
        db_user.email = user.email
    
    db.commit()
    db.refresh(db_user)
    return db_user



@router.delete("/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail= "User not found")

    db.delete(db_user)
    db.commit()
    return {"message":"User deleted"}
