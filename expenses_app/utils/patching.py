import logging

from expenses_app import settings


logger = logging.getLogger(__name__)


def enable_on_production_only(func):
    def inner(*args, **kwargs):
        if settings.FLAG__NOT_PRODUCTION:
            logger.warning(f"Function {func.__name__} is disabled on production")
            return
        return func(*args, **kwargs)
    return inner
