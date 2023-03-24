from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

    def wait_for_an_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(element))

    def wait_disable_for_an_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element(element))

    def wait_for_clickable_an_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(element))

    def take_ss(self, name):
        self.driver.get_screenshot_as_file(name)
