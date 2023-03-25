import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
from utilities.data import SampleData


class TestHomePage(BaseClass):
    def test_form_submit(self, get_data):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data["first_name"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_pass().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        self.select_by_visible_text(home_page.get_gender_dropdown(), "Male")
        home_page.get_radio().click()
        home_page.get_submit().click()
        msg = home_page.get_success_msg()
        assert SampleData.success_message in msg
        assert home_page.get_text_binding() == get_data["first_name"]
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param
