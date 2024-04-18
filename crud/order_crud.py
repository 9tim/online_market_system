from typing import List
from sqlalchemy.orm import Session, session
from model import Order

def get_order_by_id(boxSession: Session, _order_id: int):
    return boxSession.query(Order).filter(Order.order_id == _order_id).first()