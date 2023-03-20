import pytest
from selenium.webdriver.common.by import By


# setup data class level
# setup browser method level
# data load specific method level
@pytest.mark.usefixtures("setup_data", "setup_browser")
class TestExample:
    @pytest.mark.smoke
    def test_fix_demo_one(self, driver, setup_data):
        print("Test in heroku app demo")
        driver.get(setup_data[0])
        driver.switch_to.frame("mce_0_ifr")
        driver.find_element(By.ID, "tinymce").clear()
        # print("Load Data From DataLoad Fixture:", setup_data)
        driver.find_element(By.ID, "tinymce").send_keys(setup_data[1])

    def test_fix_demo_two(self):
        print("Test in fixtureDemo Two")

    def test_fix_demo_three(self):
        print("Test in fixtureDemo Three")
