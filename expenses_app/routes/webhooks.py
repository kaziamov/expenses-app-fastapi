from fastapi import APIRouter, types
from .. import settings

webhook_api_router = APIRouter()


@webhook_api_router.get("/")
async def root():
    return {"status": "ok"}


@webhook_api_router.post(f"/{settings.WEBHOOK_PATH}")
async def telegram_webhook(request: dict):
    from ..bots import telegram_dispather, telegram_bot
    update = types.Update(**request)
    await telegram_dispather.feed_update(bot=telegram_bot, update=update)
