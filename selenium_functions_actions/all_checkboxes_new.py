import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.orangehrm.com/"
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

checkboxes= driver.find_elements(By.XPATH, "//input[@type='checkboxes']")

for check in checkboxes:
    check.send_keys(Keys.SPACE)
    #check.click()