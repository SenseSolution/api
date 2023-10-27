import os

from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select

from schemas import UserBase, DeskBase
from database.models import User, Desk
from config import DB_URL
from database.core import engine, sessionmaker


app = FastAPI(title="todo api", version="1.0.1")

async def get_session() -> AsyncSession:
    db = sessionmaker()
    try:
        yield db
    finally:
        await db.close()

@app.get("/")
async def main():
    return {"message": "Hello!"}

@app.post("/users")
async def create_user(user: UserBase, session: AsyncSession = Depends(get_session)):
    try:
        u = User(
            username=user.username,
            name=user.name
        )
        
        session.add(u)
        await session.commit()
        await session.refresh(u)
        return u
    except:
        return HTTPException(409, "This username is already exists")


@app.get("/users")
async def get_users(session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(User))
    usrs = results.scalars().all()
    return {"users": usrs}

@app.get('users/{username}')
async def get_user(username: str):
    pass
