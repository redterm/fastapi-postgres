from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, primary_key=True, )
    hashed_password = Column(String, nullable=False)

