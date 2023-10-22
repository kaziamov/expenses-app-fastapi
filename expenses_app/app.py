import logging

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import settings
from .controllers.webhooks import register_webhook
from .handlers import messages_handler
from .routes import webhook_api_router
from .views.admin import admins_view
from .bots import telegram_bot, telegram_dispather

logger = logging.getLogger(__name__)

fastapi_app = FastAPI()
# admins_view.mount_to(fastapi_app)
fastapi_app.include_router(webhook_api_router)
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fastapi_app.get("/")
async def root():
    return {"message": "ok"}


@fastapi_app.on_event("startup")
async def on_startup():
    logger.info("Starting up actions")
    await register_webhook(settings.WEBHOOK_DOMAIN)
    telegram_dispather.include_router(messages_handler)


@fastapi_app.on_event("shutdown")
async def on_shutdown():
    await telegram_bot.session.close()