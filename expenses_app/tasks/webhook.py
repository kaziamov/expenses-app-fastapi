import asyncio
import logging

from ..controllers.webhooks import register_webhook

logger = logging.getLogger(__name__)


# async def update_register_url_task(cooldown: int = 7200):
#     """Update webhook url every 60 minutes"""
#     logger.info("check_new_comments_to_analyze: Started")
#     while True:
#         webhook_url = await generate_webhook_url()
#         await register_webhook(webhook_url)
#         await asyncio.sleep(cooldown)