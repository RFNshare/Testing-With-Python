from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
