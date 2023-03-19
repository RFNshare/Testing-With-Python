import pytest
from selenium.webdriver.common.by import By


# setup data class level
# setup browser method level
# data load specific method level
@pytest.mark.usefixtures("setup_data", "setup_browser")
class TestExample:
    def test_fix_demo_one(self, driver, data_load):
        print("Test in heroku app demo")
        driver.get(data_load[0])
        driver.switch_to.frame("mce_0_ifr")
        driver.find_element(By.ID, "tinymce").clear()
        print("Load Data From DataLoad Fixture:", data_load)
        driver.find_element(By.ID, "tinymce").send_keys(data_load[1])

    def test_fix_demo_two(self):
        print("Test in fixtureDemo")

    def test_fix_demo_three(self):
        print("Test in fixtureDemo")
