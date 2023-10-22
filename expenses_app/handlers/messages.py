import logging

from aiogram import Router, types

messages_handler = Router()
logger = logging.getLogger(__name__)


@messages_handler.message()
async def start(message: types.Message):
    await message.reply("Message cathed")
