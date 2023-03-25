import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data import SampleData


class TestHomePage(BaseClass):
    def test_form_submit(self, get_data):
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data[0])
        home_page.get_email().send_keys(get_data[1])
        home_page.get_pass().send_keys(get_data[2])
        home_page.get_checkbox().click()
        self.select_by_visible_text(home_page.get_gender_dropdown(), "Male")
        home_page.get_radio().click()
        home_page.get_submit().click()
        msg = home_page.get_success_msg()
        assert SampleData.success_message in msg
        assert home_page.get_text_binding() == get_data[0]
        self.driver.refresh()

    @pytest.fixture(
        params=[("Abdullah Al", "aalfaroque@gmail.com", "12345"), ("Faroque", "rfnshare@gmail.com", "4321")])
    def get_data(self, request):
        return request.param
