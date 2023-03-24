from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    msg = (By.CLASS_NAME, "alert-success")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_pass(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_radio(self):
        return self.driver.find_element(*HomePage.radio)

    def get_success_msg(self):
        return self.driver.find_element(*HomePage.msg).text
