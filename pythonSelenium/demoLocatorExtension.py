import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

# Find by Link-text
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot password").click()
driver.find_element(By.XPATH, "//form//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("123456")
# Partial Match by Text
# driver.find_element(By.XPATH, "//*[contains(text(), 'Save New')]").click()
# Exact Match by Text
# driver.find_element(By.XPATH, "//*[text() = 'Save New Password']").click()
driver.find_element(By.CSS_SELECTOR, "button[type^='sub']").click()
time.sleep(5)
