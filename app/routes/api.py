from typing import Generator
from app.routes.endpoints import users, authentication

from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(authentication.router, prefix="/auth", tags=["auth"])


