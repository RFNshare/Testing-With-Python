from utilities.locators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = HomePageLocators

    def shop_items(self):
        return self.driver.find_element(*self.locator.shop)

    def get_name(self):
        return self.driver.find_element(*self.locator.name)

    def get_email(self):
        return self.driver.find_element(*self.locator.email)

    def get_pass(self):
        return self.driver.find_element(*self.locator.password)

    def get_checkbox(self):
        return self.driver.find_element(*self.locator.checkbox)

    def get_gender_dropdown(self):
        return self.driver.find_element(*self.locator.dropdown)

    def get_submit(self):
        return self.driver.find_element(*self.locator.submit)

    def get_radio(self):
        return self.driver.find_element(*self.locator.radio)

    def get_success_msg(self):
        return self.driver.find_element(*self.locator.msg).text

    def get_text_binding(self):
        return self.driver.find_element(*self.locator.text_bindings).get_attribute("value")
