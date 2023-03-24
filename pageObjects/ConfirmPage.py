from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from utilities.data import SampleData


class ConfirmPage(BaseClass):
    purchase_btn = (By.CSS_SELECTOR, "[value='Purchase']")
    success_msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def confirm_purchase(self):
        self.driver.find_element(By.ID, "country").send_keys(SampleData.country)
        self.wait_disable_for_an_element((By.CSS_SELECTOR, ".lds-ellipsis"))
        self.wait_for_an_element((By.CSS_SELECTOR, ".suggestions"))
        self.driver.find_element(By.LINK_TEXT, SampleData.country).click()
        self.wait_for_clickable_an_element((By.CSS_SELECTOR, ".checkbox"))
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
        self.driver.find_element(*ConfirmPage.purchase_btn).click()

    def validate_purchase(self):
        # Validate Successful Purchase
        success_message = self.driver.find_element(*ConfirmPage.success_msg).text
        assert SampleData.message in success_message
