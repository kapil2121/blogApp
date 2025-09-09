from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(id, db)