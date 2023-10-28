from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.config import DB_URL


engine = create_async_engine(
    url=DB_URL
)

sessionmaker = async_sessionmaker(
    engine,
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    db = sessionmaker()
    try:
        yield db
    finally:
        await db.close()
        