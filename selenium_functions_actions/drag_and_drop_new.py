import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)

actions = ActionChains(driver)
source_ele = driver.find_element(By.XPATH, "//a[contains(text(),'SwitchTo')]")
destination_ele= driver.find_element(By.XPATH, "//a[contains(text(),'fetch')]")
time.sleep(2)
actions.drag_and_drop(source_ele,destination_ele).perform()
time.sleep(2)
driver.close()
