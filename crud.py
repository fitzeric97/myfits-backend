from sqlalchemy.orm import Session
from models import User, Promotion
from auth import get_password_hash

def create_user(db: Session, user_data):
    user = User(
        email=user_data.email,
        fits_email=generate_fits_email(user_data.email),
        password_hash=get_password_hash(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_promotion(db: Session, promo_data):
    promo = Promotion(**promo_data.dict())
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return promo

def list_promotions(db: Session, user_id: int):
    return db.query(Promotion).filter(Promotion.user_id == user_id).all()

def delete_promotion(db: Session, promo_id: int):
    promo = db.query(Promotion).get(promo_id)
    if promo:
        db.delete(promo)
        db.commit()
        return True
    return False

def generate_fits_email(email: str) -> str:
    prefix = email
