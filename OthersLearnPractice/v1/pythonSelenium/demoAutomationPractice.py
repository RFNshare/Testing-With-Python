import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
boxes = driver.find_elements(By.CSS_SELECTOR, "input[type^='chec']")
for i in boxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break
radios = driver.find_elements(By.CSS_SELECTOR, "input[value^=radio]")
for radio in radios:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break
radios[0].click()
assert radios[0].is_selected()
time.sleep(0.1)

driver.find_element(By.CSS_SELECTOR, "input[class~='btn-style']:nth-child(3)").click()
assert driver.find_element(By.CSS_SELECTOR,
                           "div[class^='right']:nth-child(2) fieldset:nth-child(1) [placeholder*='ide']").is_displayed()
