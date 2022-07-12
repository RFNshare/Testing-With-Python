import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()
# Implicit Waiting in selenium
driver.implicitly_wait(1)
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

# Explicit wait in selenium
wait = WebDriverWait(driver, 10)
# Wait Disable
wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".promo-btn-loader")))
print("Just Now")
# Wait Enable
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".promoInfo"), "Code applied ..!"))
success = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(success)
assert "applied" in success
time.sleep(2)
