import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(URL)
driver.implicitly_wait(60)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ber")
time.sleep(3)
products = driver.find_elements(By.CSS_SELECTOR, ".product-action")
assert len(products) > 0
for product in products:
    # Chaining Locators
    product.find_element(By.CSS_SELECTOR, "button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(msg)
time.sleep(3)
