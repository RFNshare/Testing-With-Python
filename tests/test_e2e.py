import pytest
from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        # Go to shop
        home_page = HomePage(self.driver)
        home_page.shop_items().click()

        # Adding Product Into Cart
        checkout = CheckOutPage(self.driver)
        checkout.add_products()

        # Go To Checkout Page
        checkout.go_to_checkout()
        checkout.confirm_checkout().click()

        # Go To Purchase Page & Purchase
        confirm_page = ConfirmPage(self.driver)
        confirm_page.confirm_purchase()
        home_page.take_ss("final_page.png")

        # Validate Successful Purchase
        confirm_page.validate_purchase()

