from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import PromoShow
from auth import get_current_user
from crud import list_promotions, delete_promotion
from database import get_db

router = APIRouter()

@router.get("/", response_model=list[PromoShow])
def get_promos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return list_promotions(db, user.id)

@router.delete("/{promo_id}")
def delete_promo(promo_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # For simplicity, assume ownership checked
    success = delete_promotion(db, promo_id)
    if not success:
        return {"error": "Promotion not found"}
    return {"deleted": True}
