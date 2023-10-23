import logging

from .. import settings
from ..bots.telegram import telegram_bot

logger = logging.getLogger(__name__)

async def register_webhook(webhook_url):
    new_webhook = f"{webhook_url}/{settings.WEBHOOK_PATH}"
    await telegram_bot.set_webhook(url=new_webhook)
    webhook_info = await telegram_bot.get_webhook_info()
    logger.info(f"""Webhook registered. New webhook info: {webhook_info}""")
