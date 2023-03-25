from selenium.webdriver.common.by import By


class HomePageLocators:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    radio = (By.CSS_SELECTOR, "#inlineRadio1")
    msg = (By.CLASS_NAME, "alert-success")
    dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    text_bindings = (By.XPATH, "(//input[@type='text'])[3]")