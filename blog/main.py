from fastapi import Depends, FastAPI

from . import models
from .database import engine
from .routers import user, blog

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(blog.router)
