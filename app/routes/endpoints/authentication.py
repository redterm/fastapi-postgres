from typing import List, Generator
from datetime import timedelta
from ratelimit import limits, sleep_and_retry

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth_services import authenticate_user, get_current_user, is_authenticated
from app.core.config import settings
from app.core.security import create_access_token
from app.db.session import SessionLocal 
from app.schemas import Token, User, oauth2_scheme


@sleep_and_retry
@limits(calls=2, period=5)
def check_limit():
    return

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/api_key", response_model=Token)
async def login_for_access_token(db : Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    check_limit()
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
async def current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = await get_current_user(token, db=db)
    check_limit()
    return user