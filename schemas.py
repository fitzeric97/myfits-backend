from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserShow(BaseModel):
    id: int
    email: EmailStr
    fits_email: EmailStr

class PromoShow(BaseModel):
    id: int
    brand: str
    subject: str
    content: str
    received_at: datetime
    expires_at: Optional[datetime]
    is_active: bool
