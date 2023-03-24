import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.maximize_window()
URL = "https://the-internet.herokuapp.com/windows"
driver.get(URL)
driver.find_element(By.LINK_TEXT, "Click Here").click()
all_windows = driver.window_handles
print(all_windows)
driver.switch_to.window(all_windows[1])
time.sleep(2)
assert "New Window" in driver.find_element(By.TAG_NAME, "h3").text
driver.close()
driver.switch_to.window(all_windows[0])
time.sleep(2)
assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text
time.sleep(3)
driver.close()
