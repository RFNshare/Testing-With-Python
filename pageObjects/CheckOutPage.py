from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass
from utilities.data import SampleData
from utilities.locators import CheckoutPageLocators


class CheckOutPage(BasePage, BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = CheckoutPageLocators

    def add_products(self):
        # Adding Product Into Cart
        all_products = self.driver.find_elements(*self.locator.all_products_loc)
        for product in all_products:
            if product.text in SampleData.product_list:
                product.find_element(*self.locator.product).click()  # Chaining Web Elements

    def go_to_checkout(self):
        # Go To Checkout Page
        self.scroll_to_top()
        self.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
        self.wait_for_an_element((By.CSS_SELECTOR, ".btn-success"))  # Waiting for Checkout Button In Next Page

    def confirm_checkout(self):
        self.find_element(By.CSS_SELECTOR, ".btn-success").click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
