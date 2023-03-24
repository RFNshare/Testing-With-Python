import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://test.sharebus.co"
driver.get(URL)
time.sleep(5)
driver.find_element(By.XPATH, "//button[@aria-current='page']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("brainstation23@yopmail.com")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Pass@1234")
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, ".text-start").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Sharelead')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(),'Continue')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(text(),'Sharebus')]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#startPoint").send_keys("Oslo, Norway")
time.sleep(2)
lst = driver.find_elements(By.CSS_SELECTOR, "span[class='pac-matched']")
for i in lst:
    if i.text == "Oslo, Norway":
        i.click()
        break
time.sleep(2)
loc = driver.find_element(By.CSS_SELECTOR, "#startPoint").get_attribute("value")
print(loc)
assert "Oslo" in loc
time.sleep(5)
