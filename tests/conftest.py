from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from testData.ui_test_data.HomePageData import HomePageData
from utilities.excel_utils import read_configuration_data_from_excel

_driver = None


# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome", help="browser options: chrome/firefox/edge/all",
#         choices=("chrome", "firefox", "edge", "all")
#     )
#     parser.addoption(
#         "--env_name", action="store", default="qa", help="browser options: qa/dev/prod",
#         choices=("qa", "dev", "prod")
#     )
#     parser.addoption(
#         "--h", action="store", default="chrome", help="browser options: yes/no",
#         choices=("yes", "no")
#     )


@pytest.fixture(params=HomePageData.b)
def cross_browser(request):
    return request.param


# Pending Cross Browser Implementation
@pytest.fixture()
def setup(request, cross_browser):
    global _driver
    # browser_name = request.config.getoption("browser_name")
    browser_name = HomePageData.browser
    url = HomePageData.url
    headless_mode = HomePageData.h_mode
    # env_name = request.config.getoption("env_name")
    # headless_mode = request.config.getoption("h")

    if cross_browser == "chrome":
        # Adding Additional Options
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        if headless_mode == "yes":
            options.add_argument("headless")
            options.add_argument("window-size=1920,1080")
        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service, options=options)
    elif cross_browser == "firefox":
        service = Service(GeckoDriverManager().install())
        _driver = webdriver.Firefox(service=service)
    elif cross_browser == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        _driver = webdriver.Edge(service=service)

    # if env_name in ("qa", "uat"):
    #     URL = "https://rahulshettyacademy.com/angularpractice"
    # else:
    #     URL = "https://rahulshettyacademy.com/"

    _driver.get(url)
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    request.cls.driver = _driver  # Initialize driver as class variable. whoever class use this fixture they can use
    # this variable
    yield _driver
    _driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = (report.nodeid.replace("::", "_")).replace("/", "__") + ".png"
            SS_PATH = Path(__file__).parent / "../output/screenshots"
            _capture_screenshot(SS_PATH / file_name)
            if file_name:
                html = (
                    '<div><img src="../screenshots/%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    _driver.get_screenshot_as_file(name)
