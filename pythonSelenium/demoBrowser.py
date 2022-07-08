from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# service_obj = Service("../resources/chromedriver.exe")

# Add some extra option for Chrome
options = Options()
options.add_argument("start-maximized")

# Auto Download Driver & Saved into Cache
chrome_service_obj = ChromeService(ChromeDriverManager().install())
firefox_service_obj = FirefoxService(GeckoDriverManager().install())
edge_service_obj = EdgeService(EdgeChromiumDriverManager().install())

# Initialize Driver & Ready to go
driver = webdriver.Edge(service=edge_service_obj)

# Open browser & go to URL
URL = "https://rahulshettyacademy.com/"
driver.get(URL)
# assert webpage title
assert driver.title in "Rahul Shetty Academy"
# Checking Current URL
assert driver.current_url in URL
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# Minimize the window
driver.minimize_window()
# Back, Refresh & Forward the browser
driver.back()
driver.refresh()
driver.maximize_window()
driver.forward()
# Close the driver
driver.close()
