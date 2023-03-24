from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Setup Initial Values
URL = "https://rahulshettyacademy.com/angularpractice/shop"
product_list = ['iphone X', 'Blackberry']
country = "Bangladesh"
message = "Success"


# define some pre function
def wait_for_an_element(element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(element))


def wait_disable_for_an_element(element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element(element))


def wait_for_clickable_an_element(element):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(element))


# Adding Additional Options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("headless")
options.add_argument('window-size=1920,1080')

# Initialize Browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)
driver.implicitly_wait(5)

# Adding Product Into Cart
all_products = driver.find_elements(By.XPATH, "//h4/a")
for product in all_products:
    if product.text in product_list:
        product.find_element(By.XPATH, "ancestor::div[@class='card h-100']//button").click()  # Chaining Web Elements=

# Go To Checkout Page
driver.execute_script("window.scrollTo(0, 0);")
driver.get_screenshot_as_file("a.png")
driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
wait_for_an_element((By.CSS_SELECTOR, ".btn-success"))  # Waiting for Checkout Button In Next Page

# Go To Purchase Page & Purchase
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.ID, "country").send_keys(country)
wait_disable_for_an_element((By.CSS_SELECTOR, ".lds-ellipsis"))
wait_for_an_element((By.CSS_SELECTOR, ".suggestions"))
driver.find_element(By.LINK_TEXT, country).click()
wait_for_clickable_an_element((By.CSS_SELECTOR, ".checkbox"))
driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
driver.find_element(By.CSS_SELECTOR, "[value='Purchase']").click()
driver.get_screenshot_as_file("s.png")

# Validate Successful Purchase
success_message = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
assert message in success_message
driver.close()
