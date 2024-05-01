# schema.py

# Pydantic 是用於數據驗證、序列化和反序列化的庫，通常用於處理請求和響應數據。
from pydantic import BaseModel
from datetime import datetime
from typing import List

class Order(BaseModel):
    order_id: int
    user_id: int 
    total_amount: int 
    created_date: datetime 
    last_modified_date: datetime
    
class OrderItem(BaseModel):
    order_item_id: int 
    order_id: int
    product_id: int
    quantity: int
    amount: int
    
class OrderPage(BaseModel):
    limit: int
    offset: int
    total: int
    results: List[Order]