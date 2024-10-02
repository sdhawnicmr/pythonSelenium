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
hover_ele = driver.find_element(By.XPATH, "//a[contains(text(),'SwitchTo')]")
time.sleep(2)
actions.move_to_element(hover_ele).perform()
time.sleep(2)
driver.close()
