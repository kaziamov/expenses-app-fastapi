from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker

from .. import settings


def get_engine():
    if settings.FLAG__NOT_PRODUCTION:
        return create_async_engine(settings.ASYNC_TEST_DATABASE_URL)
    return create_async_engine(settings.ASYNC_DATABASE_URL)


def get_sessionmaker():
    if settings.FLAG__NOT_PRODUCTION:
        return async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
    return async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async_engine = get_engine()
Session = get_sessionmaker()
