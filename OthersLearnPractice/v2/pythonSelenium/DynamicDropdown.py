import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/dropdownsPractise"
driver.get(URL)

driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item a[id*='ui-id']")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)
picked_name = driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value")
print(picked_name)
assert "India" in picked_name
