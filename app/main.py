from fastapi import FastAPI

from app.db.session import engine
from app.models import Base
from app.core.config import settings
from app.routes.api import api_router




app = FastAPI(title=settings.PROJECT_NAME)


Base.metadata.create_all(bind=engine)



app.include_router(api_router, prefix=settings.API_V1_STR)