from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from database import get_db
from crud.product_crud import get_products_query, get_product_by_id, create_product_info, update_product_info, delete_product_info
from schemas.product_schema import ProductQueryParam, ProductPage, Product, ProductRequest
from project_enum import ProductCategory


router = APIRouter()


@router.get("/products", response_model=ProductPage, summary="查詢商品列表")
def get_products (
    category: ProductCategory = None,
    search: Optional[str] = None,
    order_by: str = "created_date",
    sort: str = "desc",
    limit: int = 10, 
    offset: int = 0, db:Session= Depends(get_db)) -> ProductPage:
    query_param = ProductQueryParam(
        category=category,
        search=search,
        order_by=order_by,
        sort=sort,
        limit=limit,
        offset=offset
    )
    
    product_list, count = get_products_query(db, query_param)
    
    page = {"limit":limit, "offset": offset, "total":count, "results":product_list}
    
    return page


@router.get("/{product_id}", response_model = Product, summary = "查詢單品商品細節")
def get_product (product_id: int, db:Session = Depends(get_db)) -> Product:
    return get_product_by_id(db, product_id)


@router.post("/products", summary = "新增商品功能")
def create_product (product_msg: ProductRequest, db: Session = Depends(get_db)):
    user_id = create_product_info(db,product_msg)
   
    return get_product_by_id(db,user_id)


@router.put("/products/{product_id}", summary = "修改商品內容")
def update_product (update_msg: ProductRequest, product_id: int, db:Session = Depends(get_db)) -> Product:    
    return update_product_info(db, product_id, update_msg)
    

@router.delete("/products/{product_id}", summary = "刪除/下架商品")    
def delete_product (product_id: int, db:Session = Depends(get_db)):
    return delete_product_info(db, product_id)
    