from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_brands():
    # Placeholder: In production, return dynamic brand list
    return ["Gap", "Nike", "Everlane", "Amazon", "Spotify", "REI", "Target", "Zara", "Uniqlo"]
