import glob
import inspect
import os
from datetime import datetime
from pathlib import Path
import pytest
from selenium.webdriver.support.select import Select
import logging.config
import imaplib
import re


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        LOGGING_CONFIG = Path(__file__).parent / 'logging.conf'
        logging.config.fileConfig(LOGGING_CONFIG)
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger

    def take_ss(self, name):
        SS_PATH = Path(__file__).parent / "../output/screenshots"
        self.driver.get_screenshot_as_file(SS_PATH / name)

    def select_by_visible_text(self, loc, text):
        select = Select(loc)
        select.select_by_visible_text(text)

    # Read current date
    def read_date(self):
        return str(datetime.today().strftime('%Y-%m-%d'))

    # function to read current date and time
    def read_datetime(self):
        return str(datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))

    # function to read raw time
    def get_raw_time(self):
        return str(datetime.today().strftime('%Y%d%H%M%S'))

    def read_time(self):
        return str(datetime.today().strftime('%H-%M-%S'))