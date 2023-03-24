import inspect
import logging.config


class BaseClass:
    def get_logger(self):
        logging.config.fileConfig("logging.conf")
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger
