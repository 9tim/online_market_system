from typing import List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import  func

from model.order_model import Order, OrderItem


def get_order_by_id(boxSession: Session, _order_id: int) -> List[OrderItem]:
    return boxSession.query(OrderItem).filter(OrderItem.order_id == _order_id)


def get_orders(boxSession: Session, _user_id: int, _limit: int, _offset:int) -> Tuple[List[Order], int]:
    
    # 使用ORM方式從資料庫中獲取訂單列表
    order_list = boxSession.query(Order).filter(Order.user_id == _user_id).order_by(Order.created_date.desc()).offset(_offset).limit(_limit).all()
    # 獲取總數
    count = boxSession.query(func.count(Order.user_id)).filter(Order.user_id == _user_id).scalar()
    
    return order_list, count
 
 
def delete_order(boxSession: Session, order_id: int) -> int:
    deleted_count = boxSession.query(Order).filter(Order.order_id == order_id).delete()
    boxSession.commit()
    
    return deleted_count