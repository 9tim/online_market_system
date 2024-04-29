import hashlib
import re
from datetime import datetime
from typing import Union

from fastapi import HTTPException
from sqlalchemy.orm import Session

from model.user_model import User
from schemas.user_schema import ResponseMSG, UserRegister, UserLogin


def get_user_by_id(boxSession: Session, _user_id: int) -> Union[ResponseMSG, None]:
    user_msg = boxSession.query(User).filter(User.user_id == _user_id).first()
    
    if user_msg:
        user_data = ResponseMSG(user_id=user_msg.user_id, email=user_msg.email, role=user_msg.role, created_date=user_msg.created_date, last_modified_date=user_msg.last_modified_date)
        return user_data
    else:
        raise HTTPException(status_code=400, detail="查無資料")
    

def get_user_by_email(boxSession: Session, _email: str) -> Union[str, None]:
    _email_msg = boxSession.query(User).filter(User.email == _email).first()
    
    if _email_msg:
       raise HTTPException(status_code=409, detail=f"{_email_msg.email} 已註冊過")
    else:
        return None

 
def create_by_user_msg(boxSession: Session, user_msg: UserRegister) -> int:
    if not is_valid_email(user_msg.email):
        raise HTTPException(status_code=400, detail="不符合電子信箱格式")
    
    get_user_by_email(boxSession,user_msg.email)
    
    #密碼加密
    hashed_password = hashlib.md5(user_msg.password.encode()).hexdigest()
    current_time = datetime.now()
    
    # 創建新的 PeopleInfo 對象，設置密碼、創建時間和最後更動時間
    new_user_info  = User(password=hashed_password, 
                          role='CUSTOMER', 
                          created_date=current_time, 
                          last_modified_date=current_time, 
                          **user_msg.model_dump(exclude={'password', 'user_id'})
                          )
    
    # 添加到資料庫，提交並刷新
    boxSession.add(new_user_info)
    boxSession.commit()
    
    return new_user_info.user_id


def login_by_request(boxSession: Session, login_msg: UserLogin) -> ResponseMSG:
    if not is_valid_email(login_msg.email):
        raise HTTPException(status_code=400, detail="不符合電子信箱格式")
    
    user_msg = boxSession.query(User).filter(User.email == login_msg.email).first()
    hashed_password = hashlib.md5(login_msg.password.encode()).hexdigest()
    
    #檢查使用者是否存在比較密碼    
    if user_msg and user_msg.password == hashed_password:
        user_data = ResponseMSG(
            user_id=user_msg.user_id, 
            email=user_msg.email, 
            role=user_msg.role, 
            created_date=user_msg.created_date, 
            last_modified_date=user_msg.last_modified_date
            )
        return user_data
    else:
        raise HTTPException(status_code=400, detail="帳號或密碼有誤")
    
    
# 檢查 email 格式是否有效
def is_valid_email(email: str) -> bool:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(email_pattern, email))