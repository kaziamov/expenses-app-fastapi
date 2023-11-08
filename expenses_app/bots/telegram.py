import logging
from aiogram import Bot, Dispatcher

from .. import settings
from ..utils.patching import enable_on_production_only

logger = logging.getLogger(__name__)


@enable_on_production_only
def get_tgbot():
    return Bot(token=settings.BOT_TOKEN, parse_mode="HTML")


telegram_bot = get_tgbot()
telegram_dispather = Dispatcher()