import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import item_router

app = FastAPI()

app.include_router(item_router.router)

@app.get("/health", summary = "health check")
async def health():
    return {"message" : "App is running properly"}

