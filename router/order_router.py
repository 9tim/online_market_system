from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm.session import Session
from crud.order_crud import get_order_by_id, get_orders, delete_order
from schemas.order_schema import OrderPage

router = APIRouter()

#訂單編號查詢
@router.get("/orders/{order_id}")
def read_order_id(order_id: int, db:Session= Depends(get_db)):
    res = get_order_by_id(db,order_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res

#查詢全部訂單
@router.get("/users/{user_id}/orders", response_model=OrderPage)
def get_user_all_orders(user_id: int, limit: int = 10, offset: int = 0, db: Session= Depends(get_db)):
    order_list, count= get_orders(db, user_id, limit, offset)
    if order_list is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    page = {"limit":limit, "offset": offset, "total":count, "results":order_list}
    return page

#取消訂單
@router.delete("/delete_order/{order_id}")
def delete_user(order_id: int, db:Session= Depends(get_db)):
    try:
        delete_order(db,order_id)
    except Exception as err:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return {"code": 0}