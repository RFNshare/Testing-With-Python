import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/angularpractice"
driver.get(URL)

# Static Dropdown
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(2)
dropdown.select_by_visible_text("Male")
time.sleep(2)
# dropdown.select_by_value("value")
