from sqlalchemy.orm import Session
from model.order_model import Order
from sqlalchemy import  func

def get_order_by_id(boxSession: Session, _order_id: int):
    return boxSession.query(Order).filter(Order.order_id == _order_id).first()

def get_orders(boxSession: Session, _user_id: int, _limit: int, _offset:int):
    
    # 使用ORM方式從資料庫中獲取訂單列表
    order_list = boxSession.query(Order).filter(Order.user_id == _user_id).order_by(Order.created_date.desc()).offset(_offset).limit(_limit).all()
    # 獲取總數
    count = boxSession.query(func.count(Order.user_id)).filter(Order.user_id == _user_id).scalar()
    return order_list, count

def delete_order(db: Session, order_id: int):
    db.query(Order).filter(Order.order_id == order_id).delete()
    db.commit()
    return True