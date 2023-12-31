import logging

from aiogram import types

from ..db.crud import get_or_create, get_all, create_obj, update_obj, get_objects, get_all_with_filter
from ..models import Category, Expense, Currency, Account

logger = logging.getLogger(__name__)

async def create_category(name: str) -> int:
    new_category = await get_or_create(Category, name=name)
    return new_category.id


async def get_all_categories() -> list[Category]:
    categories = await get_all(Category)
    return categories

async def get_all_currencies() -> list[Currency]:
    currencies = await get_all(Currency)
    return currencies

async def get_accounts(currency_id) -> list[Account]:
    accounts = await get_all_with_filter(Account, dict(currency_id=currency_id))
    return accounts


async def create_expense(description: str, amount: float) -> int:
    new_expense = await create_obj(Expense, description=description, amount=amount)
    return new_expense.id

async def update_category(expense_id: int, category_id: int) -> int:
    logger.debug(f"{__name__}.update_category: expense_id = {expense_id}, category_id = {category_id}")
    category = await update_obj(Expense, expense_id, category_id=category_id)
    return category.id

async def update_currency(expense_id: int, currency_id: int) -> int:
    logger.debug(f"{__name__}.update_currency: expense_id = {expense_id}, currency_id = {currency_id}")
    currency = await update_obj(Expense, expense_id, currency_id=currency_id)
    return currency.id

async def update_account(expense_id: int, account_id: int) -> int:
    logger.debug(f"{__name__}.update_account: expense_id = {expense_id}, account_id = {account_id}")
    account = await update_obj(Expense, expense_id, account_id=account_id)
    return account.id
