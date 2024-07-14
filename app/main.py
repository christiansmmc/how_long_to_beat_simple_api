from fastapi import FastAPI

from app.endpoints import search

app = FastAPI()

app.include_router(search.router, prefix="/search", tags=["search"])
