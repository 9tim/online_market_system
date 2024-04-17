from typing import Union

from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from crud.student_crud import get_user_by_id

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user_id/{user_id}")
def read_user_id(user_id: int, db:Session= Depends(get_db)):
    res = get_user_by_id(db,user_id)
    if res is None:
        raise HTTPException(status_code=404, detail="404 Not Found.")
    return res