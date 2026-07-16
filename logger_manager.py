from loguru import logger

logger.add(
    "observability/logs/platform.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)


def get_logger():

    return logger
