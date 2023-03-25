from pageObjects.BasePage import BasePage
from utilities.BaseClass import BaseClass
from utilities.locators import HomePageLocators


class HomePage(BasePage, BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HomePageLocators

    def shop_items(self):
        return self.find_element(*self.locator.shop)

    def get_name(self):
        self.scroll_to_down()
        return self.find_element(*self.locator.name)

    def get_email(self):
        return self.find_element(*self.locator.email)

    def get_pass(self):
        return self.find_element(*self.locator.password)

    def get_checkbox(self):
        return self.find_element(*self.locator.checkbox)

    def get_gender_dropdown(self):
        return self.find_element(*self.locator.dropdown)

    def get_submit(self):
        return self.find_element(*self.locator.submit)

    def get_radio(self):
        return self.find_element(*self.locator.radio)

    def get_success_msg(self):
        return self.find_element(*self.locator.msg).text

    def get_text_binding(self):
        return self.find_element(*self.locator.text_bindings).get_attribute("value")
