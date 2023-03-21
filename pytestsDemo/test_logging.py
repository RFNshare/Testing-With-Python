import logging

def test_logging():
    file = logging.FileHandler("logfile.log")  # File for log
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # Format of log
    file.setFormatter(formatter)  # set formatter into file

    logger = logging.getLogger(__name__)  # obj of log
    logger.addHandler(file)  # adding log into file
    logger.setLevel(logging.DEBUG)
    logger.debug("Printing a debug statement")
    logger.info("Printing a info statement")
    logger.warning("Printing a war")
    logger.error("This is an critical error")

# formatter = "%(levelname)s :%(name)s :%(message)s"
# logging.basicConfig(filename="logfile.log", encoding='utf-8', format=formatter, datefmt='%m/%d/%Y %I:%M:%S %p')

