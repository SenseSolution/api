from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import DB_URL


engine = create_async_engine(
    url=DB_URL
)

sessionmaker = async_sessionmaker(
    engine,
    expire_on_commit=False
)
