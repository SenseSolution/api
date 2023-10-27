import os

from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select

from src.schemas import UserBase, DeskBase
from src.database.models import User, Desk
from src.config import DB_URL
from src.database.core import engine, sessionmaker, get_session

from src import todo


app = FastAPI(title="todo api", version="2.0.1")
app.include_router(todo.router)


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

@app.get('/users/{username}')
async def get_user(username: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.username == username))
    usr = result.scalars().one()
    return {"users": usr}
