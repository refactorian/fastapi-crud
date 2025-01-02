from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.ShowBlog],
)
async def get_blogs(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlog,
)
async def show(
    id,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_one(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.create(request, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(
    id,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(
    id,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.destroy(id, db)
