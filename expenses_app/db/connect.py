from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from ..settings import ASYNC_DATABASE_URL

async_engine = create_async_engine(ASYNC_DATABASE_URL)
AsyncSession = sessionmaker(bind=async_engine, expire_on_commit=False)