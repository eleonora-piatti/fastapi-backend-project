from fastapi import FastAPI, Depends, HTTPException

from app.db.base import Base
from app.db.session import engine
import app.models.user

from app.routers import user


app = FastAPI()
app.include_router(user.router)

# creates physical db table
Base.metadata.create_all(bind=engine) 

