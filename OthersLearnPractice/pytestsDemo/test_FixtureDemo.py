import pytest
from selenium.webdriver.common.by import By
from OthersLearnPractice.pytestsDemo.BaseClass import BaseClass
from testData.ui_test_data.HomePageData import HomePageData


# setup data class level
# setup browser method level
# data load specific method level
@pytest.mark.usefixtures("setup_data", "setup_browser")
class TestExample(BaseClass):
    @pytest.mark.smoke
    def test_fix_demo_one(self, driver, setup_data):
        log = self.get_logger()
        log.debug("Test in heroku app demo")
        driver.get(HomePageData.url)
        # driver.switch_to.frame("mce_0_ifr")
        # driver.find_element(By.ID, "tinymce").clear()
        # # print("Load Data From DataLoad Fixture:", setup_data)
        # driver.find_element(By.ID, "tinymce").send_keys(setup_data[1])
        # log.info(f"Data Send Successfully in {setup_data[1]}")

    def test_fix_demo_two(self, cross_browser):
        log = self.get_logger()
        log.debug("Test in fixtureDemo Two")
        log.info(f"Execute Successfully in {cross_browser} Browser")

    def test_fix_demo_three(self):
        print("Test in fixtureDemo Three")
