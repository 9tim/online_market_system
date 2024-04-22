# model.py

# 建立 model 的 屬性/資料庫的column
# SQLAlchemy 是用於資料庫操作的庫，用於映射物件到資料庫表格，並執行查詢、插入和更新等操作。
from sqlalchemy import Column, Integer, DateTime, String
from database import Base

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    created_date = Column(DateTime)
    last_modified_date = Column(DateTime)