import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# expect_prod = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
driver.get(URL)
select = Select(driver.find_element(By.ID, "page-menu"))
select.select_by_value("20")
time.sleep(2)
before_sort = []
b_veg = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")
for i in b_veg:
    before_sort.append(i.text)
print("Without Sort", before_sort)
before_sort.sort()
print("With Sort", before_sort)
driver.find_element(By.CSS_SELECTOR, "th[aria-label*='Veg/fruit']").click()
a_veg = driver.find_elements(By.CSS_SELECTOR, "tr td:first-child")
after_sort = []
for i in a_veg:
    after_sort.append(i.text)
print("After Click", after_sort)
cpy = after_sort.copy()
assert before_sort == cpy
