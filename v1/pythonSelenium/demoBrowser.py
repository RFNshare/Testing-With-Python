from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def run(browser, auto):
    service_obj = ""
    driver = ""
    if browser in ("Chrome", "chrome", "c"):
        # Add some extra option for Chrome
        options = Options()
        options.add_argument("start-maximized")
        if auto in ("Yes", "yes", "ok"):
            # Auto Download Driver & Saved into Cache
            service_obj = ChromeService(ChromeDriverManager().install())
        else:
            # Manually Select driver from repository
            service_obj = ChromeService("../resources/chromedriver.exe")
        # Initialize Driver & Ready to go
        try:
            driver = webdriver.Chrome(service=service_obj, options=options)
        except Exception as e:
            print("Driver Not Valid")
        finally:
            print("Cleaning Done")
    elif browser in ("Firefox", "firefox", "f"):
        # Add some extra option for Firefox
        # options = Options()
        # options.add_argument("start-maximized")
        if auto in ("Yes", "yes", "ok"):
            # Auto Download Driver & Saved into Cache
            service_obj = FirefoxService(GeckoDriverManager().install())
        else:
            # Manually Select driver from repository
            service_obj = FirefoxService("../resources/geckodriver.exe")
        # Initialize Driver & Ready to go
        driver = webdriver.Firefox(service=service_obj)
    elif browser in ("edge", "Edge", "e"):
        # Add some extra option for Firefox
        # options = Options()
        # options.add_argument("start-maximized")
        if auto in ("Yes", "yes", "ok"):
            # Auto Download Driver & Saved into Cache
            service_obj = EdgeService(EdgeChromiumDriverManager().install())
        else:
            # Manually Select driver from repository
            service_obj = ChromeService("../resources/msedgedriver.exe")
        # Initialize Driver & Ready to go
        driver = webdriver.Edge(service=service_obj)
    # Open browser & go to URL
    try:
        URL = "https://rahulshettyacademy.com/"
        driver.get(URL)
        # assert webpage title
        assert driver.title in "Rahul Shetty Academy"
        # Checking Current URL
        assert driver.current_url in URL
        driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
        # Minimize the window
        driver.minimize_window()
        # Back, Refresh & Forward the browser
        driver.back()
        driver.refresh()
        driver.maximize_window()
        driver.forward()
        # Close the driver
        driver.close()
    except Exception as e:
        print(e, "Driver Not Valid")
    finally:
        print("Cleaning Done")


if __name__ == '__main__':
    run('c', 'n')
