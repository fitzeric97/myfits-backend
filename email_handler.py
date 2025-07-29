from models import Promotion
from datetime import datetime, timedelta

def parse_inbound_email(raw_email):
    # This is a stub; real parsing will depend on provider
    # Example extraction:
    return {
        "brand": raw_email.get("brand", "Unknown"),
        "subject": raw_email.get("subject", ""),
        "content": raw_email.get("content", ""),
        "received_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(days=7),
        "is_active": True
    }
