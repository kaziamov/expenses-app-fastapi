import logging

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.methods import DeleteMessage, SendMessage
from cachetools import FIFOCache

from .. import controllers, utils, settings
from ..bots import telegram_bot

messages_handler = Router()
logger = logging.getLogger(__name__)


# Mapper for COMMANDS, C for short
C: utils.Mapper = utils.Mapper(dict(
    help="help",
    newcat="newcat",
    newexp="newexp",
))


@messages_handler.message(Command(C.help))
async def help(message: types.Message):
    await message.reply("TODO: Help message") # TODO: Help message


@messages_handler.message(Command(C.newcat))
async def new_category(message: types.Message):
    text = message.text
    logger.info(f"{__name__}.new_category: text = {text}")
    new_category = text.replace(f"/{C.newcat}", "").strip()
    if not new_category:
        await message.reply(f"Name is empty")
        return
    new_category_id = await controllers.create_category(new_category)
    await message.reply(f"Created new category: {new_category}, ID: {new_category_id}")


@messages_handler.message(Command(C.newexp))
async def new_expense(message: types.Message):
    pass



async def get_categories_keyboard(id: int, message_id: int) -> types.InlineKeyboardMarkup:
    categories = await controllers.get_all_categories()
    """Inline keyboard with categories"""
    buttons = []
    for category in categories:
        buttons.append(types.InlineKeyboardButton(text=category.name, callback_data=f"set_category:{id}:{category.id}:{message_id}"))
    if not buttons:
        return []
    keyboard = types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[buttons])
    return keyboard


async def get_currencies_keyboard(id: int, message_id: int) -> types.InlineKeyboardMarkup:
    currencies = await controllers.get_all_currencies()
    """Inline keyboard with currencies"""
    buttons = []
    for currency in currencies:
        buttons.append(types.InlineKeyboardButton(text=currency.name, callback_data=f"set_currency:{id}:{currency.id}:{message_id}"))
    if not buttons:
        return []
    keyboard = types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[buttons])
    return keyboard


async def get_accounts_keyboard(id: int, currency_id, message_id: int) -> types.InlineKeyboardMarkup:
    """Inline keyboard with accounts"""
    accounts = await controllers.get_accounts(currency_id)
    buttons = []
    for account in accounts:
        buttons.append(types.InlineKeyboardButton(text=account.name, callback_data=f"set_account:{id}:{account.id}:{message_id}"))
    if not buttons:
        return []
    keyboard = types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[buttons])
    return keyboard


@messages_handler.callback_query()
async def callback_query_handler(query: types.CallbackQuery):
    # logger.debug(f"{__name__}.callback_query_handler: query = {query}")
    message = query.message
    # logger.debug(f"{__name__}.callback_query_handler: message = {message}")
    message_id = message.message_id
    logger.debug(f"{__name__}.callback_query_handler: message_id = {message_id}")
    chat_id = message.chat.id
    logger.debug(f"{__name__}.callback_query_handler: chat_id = {chat_id}")
    if not hasattr(query, "data"):
        logger.info(f"{__name__}.callback_query_handler: No data in query")
        return
    query_split_data = query.data.split(":")
    action = query_split_data
    expense_id, target_id, original_message_id = [int(i) for i in query_split_data[1:]]
    logger.debug(f"{__name__}.callback_query_handler: {query_split_data}")
    match action:
        case "set_category":
            await controllers.update_category(expense_id, target_id)
        case "set_currency":
            await controllers.update_currency(expense_id, target_id)
            accounts_keyboard = await get_accounts_keyboard(expense_id, target_id, original_message_id)
            logger.debug(f"{__name__}.callback_query_handler: accounts_keyboard = {accounts_keyboard}")
            if accounts_keyboard:
                await telegram_bot(SendMessage(
                    chat_id=message.chat.id,
                    reply_to_message_id=original_message_id,
                    text="Select category for account",
                    reply_markup=accounts_keyboard))
        case "set_account":
            await controllers.update_account(expense_id, target_id)
    logger.info(f"{__name__}.callback_query_handler: query = {query.data}")
    try:
        await message.bot.delete_message(message.chat.id, message_id)
        logger.info(f"{__name__}.callback_query_handler: Deleted message {message_id}")
    except Exception as e:
        logger.warning(f"{__name__}.callback_query_handler: Failed to delete message {message_id}: {e}")


@messages_handler.message()
async def all_messages(message: types.Message):
    message_id = message.message_id
    text = message.text
    new_expense = text.split("\n")
    try:
        description = new_expense[0]
        amount = float(new_expense[1])
    except (IndexError, ValueError):
        logger.warning(f"{__name__}.all_messages: text = {text}, new_expense = {new_expense}")
        await message.reply(f"Amount is not a number")
        return
    logger.info(f"{__name__}.all_messages: text = {text}, new_expense = {new_expense}")
    new_expense_id = await controllers.create_expense(description, amount)
    logger.info(f"{__name__}.all_messages: text = {text}, new_expense = {new_expense}")
    categories_keyboard = await get_categories_keyboard(new_expense_id, message_id)
    currencies_keyboard = await get_currencies_keyboard(new_expense_id, message_id)
    if categories_keyboard:
        await message.reply("Select category for expense", reply_markup=categories_keyboard)
    if currencies_keyboard:
        await message.reply("Select currency for expense", reply_markup=currencies_keyboard)





