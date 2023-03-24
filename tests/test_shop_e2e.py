from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestShop(BaseClass):
    def test_e2e(self):
        # Go to shop
        home_page = HomePage(self.driver)
        home_page.shop_items().click()

        # Adding Product Into Cart
        checkout = CheckOutPage(self.driver)
        checkout.add_products()

        # Go To Checkout Page
        checkout.go_to_checkout()
        confirm_page = checkout.confirm_checkout()

        # Go To Purchase Page & Purchase
        confirm_page.confirm_purchase()
        self.take_ss("final_page.png")

        # Validate Successful Purchase
        confirm_page.validate_purchase()

