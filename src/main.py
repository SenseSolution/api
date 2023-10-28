import os

from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select

from src.schemas import UserBase, DeskBase
from src.database.models import User, Desk
from src.config import DB_URL
from src.database.core import engine, sessionmaker, get_session

from src import todo, general


app = FastAPI(title="todo api", version="2.0.2")
app.include_router(todo.router)
app.include_router(general.router)


@app.get("/")
async def main():
    return {"message": "Hello!"}

