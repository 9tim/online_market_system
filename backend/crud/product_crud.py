from typing import List, Tuple
from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from model.product_model import Product
from schemas.product_schema import ProductQueryParam, ProductRequest


def get_products_query(boxSession: Session, query_param: ProductQueryParam) -> Tuple[List[Product], int]:
    query = boxSession.query(Product)
    
    # 構建過濾條件
    if query_param.category:
       query = query.filter(Product.category == query_param.category)
       
    if query_param.search:
        query = query.filter(Product.product_name.like(f"%{query_param.search}%"))
     
    total_count = query.count()   
    
    if total_count < 1:
        raise HTTPException(status_code=404, detail="查無資料") 
        
    # 排序
    if query_param.order_by:
        if query_param.sort == "desc":
            query = query.order_by(getattr(Product, query_param.order_by).desc())
        else:
            query = query.order_by(getattr(Product, query_param.order_by))
    
    results = query.all()
    
    # 分頁
    query = query.offset(query_param.offset).limit(query_param.limit)
    
    return results, total_count


def get_product_by_id(boxSession: Session, _product_id: int) -> Product:
    res = boxSession.query(Product).filter(Product.product_id == _product_id).first()
    
    if res is None:
        raise HTTPException(status_code = 404, detail = "查無資料")
    
    return res

def create_product_info(boxSession: Session, product_msg: ProductRequest) -> int:
    current_time = datetime.now()
    
    new_product = Product(
        product_name = product_msg.product_name,
        category = product_msg.category,
        image_url = product_msg.image_url,
        price = product_msg.price,
        stock = product_msg.stock,
        description = product_msg.description,
        created_date = current_time,
        last_modified_date = current_time,
        **product_msg.model_dump(exclude = {
            'product_id',
            'product_name',
            'category',
            'image_url',
            'price',
            'stock',
            'description'})
    )
    
    # 添加新產品到資料庫
    boxSession.add(new_product)
    
    # 提交資料庫交易
    boxSession.commit()
    
    # 返回新創建的產品
    return new_product.product_id


def update_product_info(boxSession: Session, _product_id: int, update_msg: ProductRequest) -> Product:
    orignal_info  = get_product_by_id(boxSession, _product_id)
    
    if orignal_info is None:
        raise HTTPException(status_code = 404, detail = "查無資料")
    
    current_time = datetime.now()
    
    update_data = {
        "product_name": update_msg.product_name,
        "category": update_msg.category,
        "image_url": update_msg.image_url,
        "price": update_msg.price,
        "stock": update_msg.stock,
        "description": update_msg.description,
        "created_date": current_time,
        "last_modified_date": current_time,
        **update_msg.model_dump(exclude={
            'product_id',
            'product_name',
            'category',
            'image_url',
            'price',
            'stock',
            'description'
        })
    }
    
    boxSession.query(Product).filter(Product.product_id == _product_id).update(update_data)
    boxSession.commit()
    
    return get_product_by_id(boxSession, _product_id)

    
def delete_product_info(boxSession: Session, _product_id: int):
    deleted_count = boxSession.query(Product).filter(Product.product_id == _product_id).delete()
    boxSession.commit()
    
    if deleted_count < 1:
        raise HTTPException(status_code=404, detail="查無資料") 
    
    return deleted_count