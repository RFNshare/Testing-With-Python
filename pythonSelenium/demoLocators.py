import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

# Static Dropdown
gender = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
gender.select_by_visible_text("Female")
gender.select_by_index(0)


# driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').send_keys("Nothing Phone 1")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
success = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success" in success
a = driver.find_elements(By.XPATH, '//input[@type="text"]')
print(a[2].get_attribute("value"))
for i in a:
    print(i.is_displayed())
print(driver.find_element(By.CLASS_NAME, "alert-success").value_of_css_property("padding-right"))
time.sleep(5)
driver.close()
