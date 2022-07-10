import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# Inspecting Element By ID, Xpath, CSSSelector, Classname, Name
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Abdullah")
driver.find_element(By.NAME, "email").send_keys("randomemail@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# xpath: //tagname[@attribute='value']
# css: tagname[attribute='value'] / #id, .classname
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
driver.find_element(By.XPATH,'(//input[@type="text"])[3]').send_keys("Nothing Phone 1")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
success = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in success
time.sleep(5)
driver.close()
