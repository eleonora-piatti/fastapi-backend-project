from pydantic import BaseModel, EmailStr # verifies if email address is valid
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None



