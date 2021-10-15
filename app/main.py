from fastapi import FastAPI

from app.db import database
from app.routers import item


app = FastAPI(
    title="Ipavlov_test_task",
    description="Test task for company Ipavlov",
)

app.include_router(item.router)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
