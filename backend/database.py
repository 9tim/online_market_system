from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 資料庫連接字符串，格式為：資料庫類型+資料庫區定://用戶名:密碼@主機地址:端口號/資料庫名
# DB_NAME = "online-market"
SQLALCHEMY_DATABASE_URL = "sqlite:///./online-market.db"

# create SQL engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# create SQL communication session and bind
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create SQL mapping table
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()