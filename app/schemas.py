from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from pydantic.fields import Field


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class UserUpdatePassword(UserBase):
    new_password: str


class User(UserBase):
    # id: int

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/api_key")