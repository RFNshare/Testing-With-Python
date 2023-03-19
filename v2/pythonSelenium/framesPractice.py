from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
URL = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(URL)
driver.switch_to.frame("courses-iframe")
lst = driver.find_elements(By.XPATH, "//div[@id='showHeader']//b")
print(lst[0].text)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)
