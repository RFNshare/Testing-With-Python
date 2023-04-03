import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

expect_prod = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(URL)
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ber")
time.sleep(3)
products = driver.find_elements(By.XPATH, "//div[@class='product-action']")
prod_list = []
assert len(products) > 0
for product in products:
    # Chaining Locators
    prod_list.append(product.find_element(By.XPATH, "parent::div/h4").text)
    product.find_element(By.CSS_SELECTOR, "button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
assert "applied" in msg
prices = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) .amount")
total_price = 0
for price in prices:
    total_price += int(price.text)
assert int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) == total_price
assert float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text) < total_price
# for i, j in zip(prod_list, expect_prod):
#     if i == j:
#         pass
#     else:
#         raise Exception("Product Not Matching")
assert expect_prod == prod_list

time.sleep(3)
