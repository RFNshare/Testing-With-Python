import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(URL)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ber")
time.sleep(3)
products = driver.find_elements(By.CSS_SELECTOR, ".product-action")
assert len(products) > 0
for product in products:
    # Chaining Locators
    product.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(3)
