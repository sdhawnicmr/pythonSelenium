from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.ID, "login-button").click()

driver.close()