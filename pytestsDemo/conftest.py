import pytest


# Scope on class level
@pytest.fixture(scope="class")
def setup_data():
    print("Initialize Variables For Set...")
    yield
    print("Cleanup Test Cases Data ...")


# Scope on module level
@pytest.fixture()
def setup_browser():
    print("Open Browser...")
    yield
    print("Teardown Browser ...")

# @pytest.fixture
# def driver():
#     _driver = Chrome()
#     yield _driver
#     _driver.quit()
#
#
# @pytest.fixture
# def login(driver, base_url, user):
#     driver.get(urljoin(base_url, "/login"))
#     page = LoginPage(driver)
#     page.login(user)
#
#
# @pytest.fixture
# def landing_page(driver, login):
#     return LandingPage(driver)