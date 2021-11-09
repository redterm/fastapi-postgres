from typing import List, Generator
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.auth_services import is_authenticated
from app import main as api
from app.schemas import User, UserCreate, UserUpdatePassword, oauth2_scheme
from app.crud import get_users, create_user, update_password
from app.db.session import SessionLocal 


router = APIRouter()

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.post("/", response_model=User)
async def create_users(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user(db=db, user=user)
    

@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = await get_users(db=db, skip=skip, limit=limit)
    return users


@router.put("/reset_password")
async def reset_password(user: UserUpdatePassword ,token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if is_authenticated(token,db):
      await update_password(user, db)
    return status.HTTP_200_OK