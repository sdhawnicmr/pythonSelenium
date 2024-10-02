from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://realpython.com/")

dd_ele= driver.find_element(By.ID, "id value")
target_dd_value= "India"
select= Select(dd_ele)

for option in select.options:
    if option.text == target_dd_value:
        print(f" selection {target_dd_value} ")
        break
    else:
        print(f"selection {target_dd_value} not fount ")

driver.quit()