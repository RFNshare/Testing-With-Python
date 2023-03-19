import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service_obj = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[class~='inputs']").send_keys("Ind")
time.sleep(2)
search_results = driver.find_elements(By.CSS_SELECTOR, "li[class^='ui'] a")
print(f"Found Total {len(search_results)} Countries")
# lst = []
# a = 0
# for i in search_results:
#     a += 1
#     print("Inserting " + i.text + " into list", end='')
#     for j in range(a):
#         print(".", end='')
#     lst.append(i.text)
#     print("\n")
#     time.sleep(0.5)
# print(lst)
for i in search_results:
    if i.text == "India":
        i.click()
assert "India" in driver.find_element(By.CSS_SELECTOR, "input[class~='inputs']").get_attribute("value")
