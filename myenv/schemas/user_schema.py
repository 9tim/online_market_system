# schema.py

# Pydantic 是用於數據驗證、序列化和反序列化的庫，通常用於處理請求和響應數據。
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_id: int 
    email: str
    password: str
    created_date: datetime 
    last_modified_date: datetime
    
class UserRegister(BaseModel):
    email: str
    password: str
    
class UserLogin(BaseModel):
    email: str
    password: str
    
class ResponseMSG(BaseModel):
    user_id: int 
    email: str
    role: str
    created_date: datetime 
    last_modified_date: datetime