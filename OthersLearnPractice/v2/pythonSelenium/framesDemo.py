import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://the-internet.herokuapp.com/iframe"
driver.get(URL)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Writing Some Texts")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
driver.quit()
