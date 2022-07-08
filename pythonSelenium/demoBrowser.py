from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# service_obj = Service("../resources/chromedriver.exe")

# Auto Download Driver & Saved into Cache
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)
driver.get("https://github.com/SeleniumHQ/selenium/tree/trunk/py")
