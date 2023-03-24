import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")
# options.add_argument("--user-data-dir=C:/Users/rfnsh/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--test-type")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-translate")
options.add_argument("--disable-notifications")
options.add_argument("--disable-gpu")
options.add_argument("--disable-application-cache")
options.add_argument("--no-sandbox")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--window-size=1280,800")
options.experimental_options["prefs"] = {
    "logging.browser.enable": "false"}

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.implicitly_wait(5)
URL = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(URL)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("s.png")
time.sleep(2)
