import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/AutomationPractice"
driver.get(URL)

checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radio in radios:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break

# Select By Index
radios[0].click()
assert radios[0].is_selected()

assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
assert not driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()

time.sleep(2)
