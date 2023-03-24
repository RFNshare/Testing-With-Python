import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser options: chrome/firefox/edge/all",
        choices=("chrome", "firefox", "edge", "all")
    )


@pytest.fixture(params=["chrome", "firefox", "edge"])
def cross_browser(request):
    return request.param

# Pending Cross Browser Implementation
@pytest.fixture(scope="class")
def setup(request):
    _driver = None
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # Adding Additional Options
        options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")
        # options.add_argument("headless")
        # options.add_argument('window-size=1920,1080')
        service = Service(ChromeDriverManager().install())
        service = Service(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = Service(GeckoDriverManager().install())
        _driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        _driver = webdriver.Edge(service=service)

    URL = "https://rahulshettyacademy.com/angularpractice/shop"
    # Initialize Browser

    _driver.get(URL)
    _driver.implicitly_wait(5)
    _driver.maximize_window()
    request.cls.driver = _driver  # Initialize driver as class variable. whoever class use this fixture they can use
    # this variable
    yield _driver
    _driver.quit()
