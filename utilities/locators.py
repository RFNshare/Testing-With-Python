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


class CheckoutPageLocators:
    all_products_loc = (By.XPATH, "//h4/a")
    product = (By.XPATH, "ancestor::div[@class='card h-100']//button")


class ConfirmPageLocators:
    purchase_btn = (By.CSS_SELECTOR, "[value='Purchase']")
    success_msg = (By.CSS_SELECTOR, "[class*='alert-success']")
    country = (By.ID, "country")
