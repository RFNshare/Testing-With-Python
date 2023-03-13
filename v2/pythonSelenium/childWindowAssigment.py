import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(4)
URL = "https://rahulshettyacademy.com/loginpagePractise/"
driver.get(URL)
driver.find_element(By.PARTIAL_LINK_TEXT, "Free Access").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
txt = driver.find_element(By.CSS_SELECTOR, "[class='im-para red']").text
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", txt)
driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(emails[0])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("learning")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.NAME, "signin").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='alert-danger']")))
err_txt = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-danger']").text
assert "Incorrect" in err_txt