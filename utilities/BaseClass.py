import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
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

    def select_by_visible_text(self, loc, text):
        select = Select(loc)
        select.select_by_visible_text(text)

    def hover_on_an_element(self, loc):
        action = ActionChains(self.driver)
        action.move_to_element(loc).perform()

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
