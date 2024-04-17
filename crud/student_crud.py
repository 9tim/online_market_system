from typing import List
from sqlalchemy.orm import Session, session
from model import PeopleInfo

def get_user_by_id(boxSession: Session, _id: int):
    return boxSession.query(PeopleInfo).filter(PeopleInfo.id == _id).first()