import sys
from typing import Optional

from django.conf import settings
from loguru import logger


class LoggingService:
    def __init__(
        self,
        debug: Optional[bool] = settings.DEBUG,
        **kwargs,
    ):
        super().__init__()
        logger.remove()
        self.set_log_level()

    def set_log_level(self):
        level = "DEBUG" if settings.DEBUG else "INFO"
        format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> |"
            "<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:"
            "<cyan>{line}</cyan> - <level>{message}</level>"
        )
        logger.add(sink=sys.stderr, format=format, level=level)
        # logger.add(sink=sys.stderr, level=level)

    def info(self, message):
        logger.info(message)

    def warn(self, message):
        logger.warning(message)

    def debug(self, message):
        logger.debug(message)

    def error(self, message):
        logger.error(message)
