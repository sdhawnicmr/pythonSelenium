import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.orangehrm.com/"

dropdown_ele = driver.find_element(By.ID, 'idvalue')
select = Select(dropdown_ele)
select.select_by_value("India")
select.select_by_visible_text("some text")
select.select_by_index(1)
