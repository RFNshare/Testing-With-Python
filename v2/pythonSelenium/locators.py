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
driver.find_element(By.NAME, "name").send_keys("Faroque")
driver.find_element(By.NAME, "email").send_keys("aalfaroque@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(5)
