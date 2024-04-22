from fastapi import FastAPI
from router.order_router import routerO
from router.user_router import routerU

app = FastAPI()

app.include_router(routerU)
app.include_router(routerO)