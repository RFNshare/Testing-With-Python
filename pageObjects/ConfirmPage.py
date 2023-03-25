from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data import SampleData
from utilities.locators import ConfirmPageLocators


class ConfirmPage(BasePage, BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = ConfirmPageLocators

    def confirm_purchase(self):
        self.find_element(By.ID, "country").send_keys(SampleData.country)
        self.wait_disable_for_an_element((By.CSS_SELECTOR, ".lds-ellipsis"))
        self.wait_for_an_element((By.CSS_SELECTOR, ".suggestions"))
        self.find_element(By.LINK_TEXT, SampleData.country).click()
        self.wait_for_clickable_an_element((By.CSS_SELECTOR, ".checkbox"))
        self.find_element(By.CSS_SELECTOR, ".checkbox").click()
        self.find_element(*self.locator.purchase_btn).click()

    def validate_purchase(self):
        # Validate Successful Purchase
        success_message = self.find_element(*self.locator.success_msg).text
        assert SampleData.message in success_message
