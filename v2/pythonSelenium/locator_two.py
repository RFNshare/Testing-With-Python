import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/client"
driver.get(URL)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input[contains(@placeholder,\"email\")]").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input[placeholder*='Pass']").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[contains(text(),\"Save\")]").click()
time.sleep(1)
msg = driver.find_element(By.CSS_SELECTOR, "div[aria-label*=\"Password\"]").text
# msg = driver.find_element(By.XPATH, "//*[contains(text(),'Successfully')]").text
print(msg)
assert "Successfully" in msg
time.sleep(5)
