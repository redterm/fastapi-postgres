from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import User, UserUpdatePassword
from app import models
from app.core.security import get_password_hash


def get_user_by_username(db: Session, username):
    return db.query(models.User).filter(models.User.username == username).first()

async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

async def create_user(db: Session, user: User):
    hashed_password = get_password_hash(user.password)
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def update_password(user: UserUpdatePassword, db: Session):
    db_user = get_user_by_username(db, username=user.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="Username or password is incorrect")
    hashed_password = get_password_hash(user.new_password)
    db.query(models.User).filter(models.User.username == user.username).update({models.User.hashed_password : hashed_password }, synchronize_session = False)
    db.commit()
