from fastapi import FastAPI
from router.order_router import router as order_router
from router.user_router import router as user_router

app = FastAPI()

app.include_router(order_router, prefix="/order", tags=["訂單功能"])
app.include_router(user_router, prefix="/user", tags=["會員功能"])