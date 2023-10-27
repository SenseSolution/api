import os

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from schemas import UserBase, DeskBase
from database.models import User, Desk
from config import DB_URL
# from database.core import engine, sessionmaker

engine = create_async_engine(
    url=DB_URL
)

sessionmaker = async_sessionmaker(
    engine,
    expire_on_commit=False
)


app = FastAPI(title="todo api", version="1.0.0")

async def get_session() -> AsyncSession:
    async with sessionmaker() as session:
        return session

@app.get("/")
async def main():
    return {"message": "Hello!"}

@app.post("/users")
async def create_user(user: UserBase):
    session = sessionmaker()
    u = User(
        username=user.username,
        name=user.name
    )
    
    await session.add(u)
    await session.commit()
    await session.refresh(u)
    return u
    
    

@app.get("/users")
async def get_users():
    pass

@app.get('users/{username}')
async def get_user(username: str):
    pass
