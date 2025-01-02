from fastapi import APIRouter, Depends, status
from .. import schemas, database
from ..repository import user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowUser,
)
async def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowUser,
)
async def show(id, db: Session = Depends(database.get_db)):
    return user.show(id, db)
