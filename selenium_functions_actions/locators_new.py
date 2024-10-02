from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = "https://www.saucedemo.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()

username = "standard_user"
password = "secret_sauce"
driver.find_element(By.ID, "id value").send_keys(username)
driver.find_element(By.ID, "id value2").send_keys(password)
driver.find_element(By.ID, "id value3").click()

driver.close()
