import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    URL = "https://rahulshettyacademy.com/angularpractice/shop"
    # Adding Additional Options
    options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    # options.add_argument("headless")
    # options.add_argument('window-size=1920,1080')

    # Initialize Browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(URL)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver  # Initialize driver as class variable. whoever class use this fixture they can use
    # this variable
    yield driver
    driver.quit()
