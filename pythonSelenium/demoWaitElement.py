import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "[placeholder*='for']").send_keys("ber")
time.sleep(3)
products = driver.find_elements(By.CSS_SELECTOR, "div[class^='product'] [type*='button']")
assert len(products) > 0
for product in products:
    product.click()
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.CSS_SELECTOR, "div[class^='action']:nth-child(2) button[type='button']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
success = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(success)
assert "applied" in success
time.sleep(2)
