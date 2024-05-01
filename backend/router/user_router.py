from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from database import get_db
from crud.user_crud import create_by_user_msg, get_user_by_id, login_by_request
from schemas.user_schema import UserLogin, UserRegister


router = APIRouter()


@router.post("/register", summary="註冊功能")
def register (user_msg: UserRegister, db: Session= Depends(get_db)):
    user_id = create_by_user_msg(db,user_msg)
   
    return get_user_by_id(db,user_id)


@router.post("/login", summary="登入功能")
def login (login_msg: UserLogin, db: Session= Depends(get_db)):
    return login_by_request(db, login_msg)
