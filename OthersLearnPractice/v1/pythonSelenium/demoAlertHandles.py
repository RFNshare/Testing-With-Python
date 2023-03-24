import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Faroque")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Faroque" in alert.text
alert.accept()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Faroque")
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
time.sleep(1)
alert.dismiss()
time.sleep(3)
