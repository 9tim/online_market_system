from typing import List
from sqlalchemy.orm import Session, session
from model import Order

def get_order_by_id(boxSession: Session, _order_id: int):
    return boxSession.query(Order).filter(Order.order_id == _order_id).first()

def get_orders(boxSession: Session, _user_id: int):
    return boxSession.query(Order).filter(Order.user_id == _user_id).all()

def delete_order(db: Session, order_id: int):
    db.query(Order).filter(Order.order_id == order_id).delete()
    db.commit()
    return True