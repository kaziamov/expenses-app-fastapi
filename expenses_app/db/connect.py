from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from ..settings import ASYNC_DATABASE_URL

async_engine = create_async_engine(ASYNC_DATABASE_URL)
AsyncSession = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
