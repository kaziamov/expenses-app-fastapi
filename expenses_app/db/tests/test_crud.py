import pytest

from expenses_app.db import Session
from expenses_app.db.crud import *
from expenses_app.models import *

# BaseSQLModel.metadata.create_all(bind=async_engine)


# @pytest.fixture(scope='session', autouse=True)
async def init_models():
    async with Session() as conn:
        await conn.run_sync(BaseSQLModel.metadata.drop_all)
        await conn.run_sync(BaseSQLModel.metadata.create_all)


@pytest.fixture(scope="session", autouse=True)
async def create_tables():
    async with Session() as conn:
        try:
            await conn.run_sync(BaseSQLModel.metadata.create_all)
            yield conn
        finally:
            await conn.run_sync(BaseSQLModel.metadata.create_all)



@pytest.mark.asyncio
async def test_flow_create_expense_with_new_category_and_currency(create_tables):
    conn = create_tables
    category_1 = await create_obj(Category, name='test')
    currency_1 = await create_obj(Currency, name='test', code='test')
    account_1 = await create_obj(Account, name='test', currency_id=currency_1.id)
    expense_1 = await create_obj(Expense, description='test', amount=100, category_id=category_1.id,
        account_id=account_1.id, currency_id=currency_1.id)
