import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Scope on class level
@pytest.fixture(scope="class")
def setup_data():
    print("Initialize Variables For Set...")
    yield
    print("Cleanup Test Cases Data ...")


@pytest.fixture
def data_load():
    print("Data...")
    return ["https://the-internet.herokuapp.com/tinymce", "Abdullah Al Faroque"]


# Scope on module level
@pytest.fixture()
def setup_browser():
    print("Open Browser...")
    yield
    print("Teardown Browser ...")


@pytest.fixture
def driver():
    print("Open Browser Original...")
    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service)
    _driver.implicitly_wait(5)
    yield _driver
    time.sleep(1)
    _driver.quit()
    print("Teardown Browser Original...")
    return _driver
#
#
# @pytest.fixture
# def login(driver, base_url, user):
#     driver.get(urljoin(base_url, "/login"))
#     page = LoginPage(driver)
#     page.login(user)
#
#
# @pytest.fixture
# def landing_page(driver, login):
#     return LandingPage(driver)
