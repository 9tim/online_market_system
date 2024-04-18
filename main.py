from fastapi import FastAPI
from router.order_router import router

app = FastAPI()

app.include_router(router)