import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from testData.ui_test_data.HomePageData import HomePageData


# Scope on class level
@pytest.fixture(scope="class")
def setup_data():
    print("Initialize Variables For Set...")
    lst = ["https://example.com/", "Abdullah Al Faroque"]
    yield lst
    print("Cleanup Test Cases Data ...")


# Scope on module level
@pytest.fixture()
def setup_browser(cross_browser):
    print(f"Open {cross_browser} Browser...")
    yield cross_browser
    print(f"Teardown {cross_browser} Browser ...")


# @pytest.fixture(params=[("chrome", "raju", "pass"), ("firefox", "raju"), "edge"]) # For send more data per run
@pytest.fixture(params=HomePageData.b)
def cross_browser(request):
    return request.param


@pytest.fixture()
def driver(cross_browser):
    _driver = None
    # print("Open Browser Original...")
    if cross_browser == "chrome":
        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service)
    elif cross_browser == "firefox":
        service = Service(GeckoDriverManager().install())
        _driver = webdriver.Firefox(service=service)
    else:
        service = Service(EdgeChromiumDriverManager().install())
        _driver = webdriver.Edge(service=service)
    _driver.implicitly_wait(5)
    yield _driver
    time.sleep(1)
    _driver.quit()
    # print("Teardown Browser Original...")


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
