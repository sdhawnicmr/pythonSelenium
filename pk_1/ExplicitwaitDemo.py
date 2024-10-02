from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.ID, "login-button").click()

#Creating a WebDriverWait object
wait = WebDriverWait(driver, 10)

#Using ExpectedCondition
ele= wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='idvalue']")))
ele.click()

driver.close()





