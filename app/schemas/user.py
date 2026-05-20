from pydantic import BaseModel, EmailStr # verifies if email address is valid

class UserCreate(BaseModel):
    email: EmailStr