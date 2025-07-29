from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from crud import create_promotion
from database import get_db
from email_handler import parse_inbound_email

router = APIRouter()

@router.post("/inbound")
async def inbound_email(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    parsed = parse_inbound_email(data)
    # Attach to some user—MVP can hardcode/test, production should look up
    user_id = 1  # Replace with actual lookup if available
    promo_data = parsed
    promo_data["user_id"] = user_id
    promo = create_promotion(db, promo_data)
    return {"id": promo.id, "status": "received"}
