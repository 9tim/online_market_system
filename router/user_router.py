from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm.session import Session
from schemas.user_schema import UserLogin, UserRegister
from crud.user_crud import register_by_user_msg, get_user_by_id

routerU = APIRouter()

@routerU.post("/users/register")
def register (user_msg: UserRegister, db: Session= Depends(get_db)):
    user_id = register_by_user_msg(db,user_msg)
   
    return get_user_by_id(db,user_id)