import inspect
import logging.config
from pathlib import Path


class BaseClass:
    def get_logger(self):
        LOGGING_CONFIG = Path(__file__).parent / 'logging.conf'
        logging.config.fileConfig(LOGGING_CONFIG)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger
