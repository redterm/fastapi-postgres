import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):

    db_url: str = Field(..., env='DATABASE_URL')
    PROJECT_NAME: str = "practice python"

    API_V1_STR: str = "/api"

    SECRET_KEY:str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30


settings = Settings()