import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.orangehrm.com/"
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#check
driver.find_element(By.ID, "id value").click()
time.sleep(2)
#Uncheck
driver.find_element(By.ID, "id value").click()