# model.py

# create model attribute/column
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

# relationship with ORM
#from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy.orm import relationship

class PeopleInfo(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=30))