import logging.config
from pathlib import Path


def test_logging():
    LOGGING_CONFIG = Path(__file__).parent / "logging.conf"
    logging.config.fileConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    logger.debug("Printing a debug statement")
    logger.info("Printing a info statement")
    logger.warning("Printing a war")
    logger.error("This is an critical error")
    logger.critical("Critical Issues")


# Another Way One
# def test_logging():
#     # set up logging to file
#     file = logging.FileHandler("logfile.log")  # File for log
#     formatter = logging.Formatter("%(levelname)s :%(name)s :%(message)s :%(asctime)s")  # Format of log
#     file.setFormatter(formatter)  # set formatter into file
#
#     # set up logging to file
#     logger = logging.getLogger(__name__)  # obj of log
#     logger.addHandler(file)  # adding log into file
#     logger.setLevel(logging.DEBUG)
#     logger.debug("Printing a debug statement")
#     logger.info("Printing a info statement")
#     logger.warning("Printing a war")
#     logger.error("This is an critical error")

# Another Way Two
# formatter = "%(levelname)s :%(name)s :%(message)s :%(asctime)s"  # Format of log
# logging.basicConfig(filename="logfile.log", format=formatter, datefmt='%m/%d/%Y %I:%M:%S %p',
#                     level=logging.WARNING)  # File for log
# logger = logging.getLogger(__name__)  # obj of log
# logger.warning("Printing a war")
# logger.error("This is a critical error")
