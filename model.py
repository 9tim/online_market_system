# model.py

# create model attribute/column
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

# relationship with ORM
#from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "order"
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    total_amount = Column(Integer)
    created_date = Column(DateTime)
    last_modified_date = Column(DateTime)
    
class OrderItem(Base):
    __tablename__= "order_item"
    order_item_id  = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    amount = Column(Integer)