import logging
from typing import List, Dict

from cachetools import LFUCache
from sqlalchemy import select

from ..db import AsyncSession
from ..models import BaseSQLModel
from ..settings import CACHE_SIZE

logger = logging.getLogger(__name__)
cache = LFUCache(maxsize=CACHE_SIZE)

async def create_obj(model: BaseSQLModel, **params) -> BaseSQLModel:
    """Create object in db"""
    logger.debug(f"{__name__}.create_obj: model = {model}, params = {params}")
    new_obj = model(**params)
    async with AsyncSession() as conn:
        conn.add(new_obj)
        await conn.commit()
        await conn.refresh(new_obj)
    return new_obj


async def get_obj(model: BaseSQLModel, **filters) -> BaseSQLModel:
    """Get object from db"""
    key = f"{model.__name__}{filters}"
    query = select(model).filter_by(**filters)
    logger.debug(f"{__name__}.get_obj: query = {query}")
    async with AsyncSession() as conn:
        result = await conn.execute(query)
    logger.debug(f"{__name__}.get_obj: result = {result}")
    obj = result.scalars().first()
    logger.debug(f"{__name__}.get_obj: obj = {obj}")
    return obj

async def get_all(model: BaseSQLModel) -> List[BaseSQLModel]:
    """Get objects from db"""
    query = select(model)
    async with AsyncSession() as conn:
        result = await conn.execute(query)
    logger.debug(f"{__name__}.get_all: result = {result}")
    objects = result.scalars().all()
    logger.debug(f"{__name__}.get_all: obj = {objects}")
    return objects


async def get_objects(model: BaseSQLModel, filters: Dict, limit=10, offset=10) -> List[BaseSQLModel]:
    """Get objects from db"""
    query = select(model).filter_by(**filters).limit(limit).offset(offset)
    logger.debug(f"{__name__}.get_objects: query = {query}")
    async with AsyncSession() as conn:
        result = await conn.execute(query)
    logger.debug(f"{__name__}.get_objects: result = {result}")
    objects = result.scalars().all()
    logger.debug(f"{__name__}.get_objects: obj = {objects}")
    return objects


async def get_or_create(model: BaseSQLModel, **params):
    """Get object from db or create new one"""
    key = f"{model.__name__}{params}"
    obj = await get_obj(model, **params)
    if not obj:
        obj = await create_obj(model, **params)
    return obj


# async def create_or_update(model, filters: dict, **params):
#     """Create object in db or update existing one"""
#     obj = await get_or_create(model, **filters)
#     return update_obj(obj, params)


async def update_obj(model: BaseSQLModel, id: int, **params) -> BaseSQLModel:
    async with AsyncSession() as conn:
        obj = await get_obj(model, id=id)
        for key, value in params.items():
            setattr(obj, key, value)
        conn.add(obj)
        await conn.commit()
        await conn.refresh(obj)
    return obj
