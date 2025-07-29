from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Text
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    fits_email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime)
    promos = relationship("Promotion", back_populates="user")

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    brand = Column(String)
    subject = Column(String)
    content = Column(Text)
    received_at = Column(DateTime)
    expires_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    user = relationship("User", back_populates="promos")
