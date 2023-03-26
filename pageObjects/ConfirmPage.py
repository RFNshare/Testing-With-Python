from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage
from testData.ui_test_data.HomePageData import HomePageData
from testData.ui_test_data.ShopPageData import ShopData
from utilities.locators import ConfirmPageLocators


class ConfirmPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = ShopData
        self.locator = ConfirmPageLocators

    def confirm_purchase(self):
        self.send_data(self.data.country, *self.locator.country)
        self.wait_till_invisibility_of_element_located(10, *(By.CSS_SELECTOR, ".lds-ellipsis"))
        self.wait_till_visibility_of_element_located(10, *(By.CSS_SELECTOR, ".suggestions"))
        self.find_element(By.LINK_TEXT, self.data.country).click()
        self.wait_for_clickable_an_element((By.CSS_SELECTOR, ".checkbox"))
        self.click(*(By.CSS_SELECTOR, ".checkbox"))
        self.find_element(*self.locator.purchase_btn).click()

    def validate_purchase(self):
        # Validate Successful Purchase
        success_message = self.find_element(*self.locator.success_msg).text
        assert HomePageData.message in success_message
