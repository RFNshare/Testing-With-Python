import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# service = Service("../../drivers/chromedriver.exe")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/"
driver.get(URL)
assert "Rahul Shetty Academy" in driver.title
print(driver.current_url)
driver.implicitly_wait(60)
driver.back()
driver.forward()
driver.refresh()
time.sleep(5)
driver.close()
