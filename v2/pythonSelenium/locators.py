import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/angularpractice"
driver.get(URL)

# ID, Xpath, CSSSelector, CLassName, Name, LinkText
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Abdullah Al Faroque")
driver.find_element(By.NAME, "email").send_keys("aalfaroque@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath Syntext: //tag[@attribute='value']
# CSS Syntext:   tag[attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
msg = driver.find_element(By.CLASS_NAME, "alert-success").text
print(msg)
assert "Success" in msg
time.sleep(3)
