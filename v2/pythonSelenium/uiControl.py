import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
        break
time.sleep(2)
