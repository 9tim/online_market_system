from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm.session import Session
from crud.order_crud import get_order_by_id, get_orders, delete_order

router = APIRouter()

@router.get("/order_id/{order_id}")
def read_order_id(order_id: int, db:Session= Depends(get_db)):
    res = get_order_by_id(db,order_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res

@router.get("/orders/{user_id}")
def get_user_all_order(user_id: int, db: Session= Depends(get_db)):
    res = get_orders(db, user_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res

@router.delete("/delete_order/{order_id}")
def delete_user(order_id: int, db:Session= Depends(get_db)):
    try:
        delete_order(db,order_id)
    except Exception as err:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return {"code": 0}