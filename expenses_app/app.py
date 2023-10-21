import logging

from fastapi import FastAPI

from . import settings
from .controllers.webhooks import register_webhook
from .handlers import messages_handler
from .routes import webhook_api_router
from .views.admin import admins_view
from .bots import telegram_bot, telegram_dispather

logger = logging.getLogger(__name__)

app = FastAPI()
admins_view.mount_to(app)
app.include_router(webhook_api_router)


@app.get("/")
async def root():
    return {"message": "ok"}


@app.on_event("startup")
async def on_startup():
    logger.info("Starting up actions")
    await register_webhook(settings.WEBHOOK_URL)
    telegram_dispather.include_router(messages_handler)


@app.on_event("shutdown")
async def on_shutdown():
    await telegram_bot.session.close()