import pytest
from pageObjects.HomePage import HomePage
from testData.ui_test_data.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
import allure


@allure.title("Home Page - test")
@allure.description("Checking if homepage form submitted properly")
class TestHomePage(BaseClass):
    def test_form_submit(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data["first_name"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_pass().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        self.select_by_visible_text(home_page.get_gender_dropdown(), "Male")
        home_page.get_radio().click()
        home_page.get_submit().click()
        msg = home_page.get_success_msg()
        assert HomePageData.success_message in msg
        log.info("Fill up Form & Validated with email " + get_data["email"])
        assert home_page.get_text_binding() == get_data["first_name"]
        log.info("Validate Name In Second Field")
        self.driver.refresh()

    # @pytest.mark.parametrize(
    #     "browser_name",
    #     ["chrome", "firefox", "edge"],
    #     ids=["Chrome Browser TEST", "Firefox Browser TEST", "Edge Browser TEST"]
    # )
    @pytest.fixture(params=HomePageData.get_test_data("TestCase2"))
    def get_data(self, request):
        return request.param

    # @pytest.fixture(params=HomePageData.get_test_data())
    # def get_data(self, request):
    #     return request.param
