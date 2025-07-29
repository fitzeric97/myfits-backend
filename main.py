from fastapi import FastAPI
from routers import users, promos, email, brands

app = FastAPI(title="Fits Promo Organizer")

app.include_router(users.router, prefix="/auth", tags=["auth"])
app.include_router(promos.router, prefix="/promos", tags=["promos"])
app.include_router(email.router, prefix="/email", tags=["email"])
app.include_router(brands.router, prefix="/brands", tags=["brands"])
