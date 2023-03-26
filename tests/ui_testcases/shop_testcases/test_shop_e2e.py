import allure

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


@allure.title("Shop Page - test")
@allure.description("Checking purchased properly from shop")
class TestShop(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        # Go to shop
        home_page = HomePage(self.driver)
        home_page.shop_items().click()

        # Adding Product Into Cart
        checkout = CheckOutPage(self.driver)
        checkout.add_products()
        log.info("Added Product Into Carts")
        # Go To Checkout Page
        checkout.go_to_checkout()
        confirm_page = checkout.confirm_checkout()

        # Go To Purchase Page & Purchase
        confirm_page.confirm_purchase()
        log.info("Confirmed Purchase")
        self.take_ss("final_page.png")

        # Validate Successful Purchase
        confirm_page.validate_purchase()
        log.info("Validated Purchase")
