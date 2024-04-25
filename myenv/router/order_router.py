from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from database import get_db
from crud.order_crud import get_order_by_id, get_orders, delete_order
from schemas.order_schema import OrderPage, Order


router = APIRouter()


@router.get("/{order_id}", summary="查詢訂單細節功能")
def read_order_id(order_id: int, db:Session= Depends(get_db)) -> Order:
    res = get_order_by_id(db,order_id)
    
    if res is None:
        raise HTTPException(status_code=404, detail="查無資料")
    
    return res


@router.get("/users/{user_id}", response_model=OrderPage, summary="查詢訂單列表功能")
def get_user_all_orders(
    user_id: int, 
    limit: int = 10, 
    offset: int = 0, 
    db: Session= Depends(get_db)
) -> OrderPage:
    order_list, count= get_orders(db, user_id, limit, offset)
    
    if not order_list :
        raise HTTPException(status_code=404, detail="查無資料")
    page = {"limit":limit, "offset": offset, "total":count, "results":order_list}
    
    return page


@router.delete("/delete_order/{order_id}", summary="取消訂單功能")
def delete_user(order_id: int, db: Session= Depends(get_db)) -> dict:
    result=delete_order(db,order_id)
    
    return {"成功刪除筆數": result}