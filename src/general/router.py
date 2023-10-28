from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.core import get_session
from src.database.models import User
from src.schemas import UserBase

router = APIRouter(prefix="/general")


@router.post("/users")
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


@router.get("/users")
async def get_users(session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(User))
    usrs = results.scalars().all()
    return {"users": usrs}

@router.get('/users/{username}')
async def get_user(username: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User).where(User.username == username))
    usr = result.scalars().one()
    return {"users": usr}
