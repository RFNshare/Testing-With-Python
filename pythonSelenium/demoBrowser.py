from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("../resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://github.com/SeleniumHQ/selenium/tree/trunk/py")
