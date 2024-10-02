import time
import json
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

with open("tesdata.json",'r') as file:
    test_data= json.load(file)

for data in test_data['users']:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['[password]'])
    driver.find_element(By.ID, "login-button").click()
    driver.quit()