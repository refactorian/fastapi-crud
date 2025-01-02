from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
def index():
    return {"data": "blog list"}


@app.get("/blog/{id}")
def show(id: int):
    return {"item_id": id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post("/blog")
def create_blog(blog: Blog):
    return {"title": blog.title, "body": blog.body}
