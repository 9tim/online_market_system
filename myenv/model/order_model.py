# model.py

# 建立 model 的 屬性/資料庫的column
# SQLAlchemy 是用於資料庫操作的庫，用於映射物件到資料庫表格，並執行查詢、插入和更新等操作。
from sqlalchemy import Column, Integer, DateTime
from database import Base

class Order(Base):
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    total_amount = Column(Integer)
    created_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    
class OrderItem(Base):
    __tablename__= "order_item"
    order_item_id  = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    amount = Column(Integer)
    