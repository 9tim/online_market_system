from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.user_model import User
from sqlalchemy import  func
from schemas.user_schema import ResponseMSG, UserRegister
import hashlib
from datetime import datetime
import re

#Id帳號查詢
def get_user_by_id(boxSession: Session, _user_id: int):
    user_msg = boxSession.query(User).filter(User.user_id == _user_id).first()
    
    if user_msg:
        user_data = ResponseMSG(user_id=user_msg.user_id, email=user_msg.email, created_date=user_msg.created_date, last_modified_date=user_msg.last_modified_date)
        return user_data
    else:
        return None

#新增使用者資訊  
def register_by_user_msg(boxSession: Session, user_msg: UserRegister):
    # 檢查 email 格式是否有效
    if not is_valid_email(user_msg.email):
        raise HTTPException(status_code=400, detail="不符合電子信箱格式")
    
    #Email查詢與檢核  
    _email_msg = boxSession.query(User).filter(User.email == user_msg.email).first()
    
    if _email_msg:
       raise HTTPException(status_code=409, detail=f"{_email_msg.email} 已註冊過")
   
    #密碼加密
    hashed_password = hashlib.md5(user_msg.password.encode()).hexdigest()
    current_time = datetime.now()
    
    # 創建新的 PeopleInfo 對象，設置密碼、創建時間和最後更動時間
    new_user_info  = User(password=hashed_password, created_date=current_time, last_modified_date=current_time, **user_msg.model_dump(exclude={'password', 'user_id'}))
    
    # 添加到資料庫，提交並刷新
    boxSession.add(new_user_info)
    boxSession.commit()
    
    return new_user_info.user_id

def is_valid_email(email: str) -> bool:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))