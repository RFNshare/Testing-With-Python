import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument('disable-gpu')
chrome_options.add_argument('headless')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
URL = "https://expired.badssl.com/"
driver.get(URL)
print(driver.title)
time.sleep(2)
