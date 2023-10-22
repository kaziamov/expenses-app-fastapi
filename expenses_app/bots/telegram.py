import logging
from aiogram import Bot, Dispatcher

from .. import settings

logger = logging.getLogger(__name__)

telegram_bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
telegram_dispather = Dispatcher()