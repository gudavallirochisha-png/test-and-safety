import logging
import sys
from backend.app.config.settings import settings


def setup_logging():
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logger = logging.getLogger("trust_safety")
    logger.info("Structured logging initialized for Trust & Safety Platform.")
    return logger


logger = setup_logging()
