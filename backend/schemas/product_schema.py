# schema.py

# Pydantic 是用於數據驗證、序列化和反序列化的庫，通常用於處理請求和響應數據。
from pydantic import BaseModel
from datetime import datetime
from typing import List, Union

from project_enum import ProductCategory

class Product(BaseModel):
    product_id: int
    product_name: str
    category: str
    image_url: str
    price: int
    stock: int
    description: Union[str, None]
    created_date: datetime
    last_modified_date: datetime
    
class ProductQueryParam(BaseModel):
    category: Union[ProductCategory, None] = None
    search: Union[str, None] = None
    order_by: str
    sort: str
    limit: int
    offset: int 
    
class ProductRequest(BaseModel):
    product_name: str
    category: str
    image_url: str
    price: int
    stock: int
    description: Union[str, None]
    
class ProductPage(BaseModel):
    limit: int
    offset: int
    total: int
    results: List[Product]