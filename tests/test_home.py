from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data import SampleData


class TestHomePage(BaseClass):
    def test_form_submit(self):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(SampleData.name)
        home_page.get_email().send_keys(SampleData.email)
        home_page.get_pass().send_keys(SampleData.password)
        home_page.get_checkbox().click()
        self.select_by_visible_text(home_page.get_gender_dropdown(), "Male")
        home_page.get_radio().click()
        home_page.get_submit().click()
        msg = home_page.get_success_msg()
        assert SampleData.success_message in msg
