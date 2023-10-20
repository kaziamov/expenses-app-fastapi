from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from expenses_app.settings import ASYNC_DATABASE_URL

engine = create_async_engine(ASYNC_DATABASE_URL)
Session = sessionmaker(bind=engine, expire_on_commit=False)