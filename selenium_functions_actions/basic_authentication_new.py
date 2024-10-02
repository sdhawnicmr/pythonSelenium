import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

username= "admin"
password= "admin"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#"https://admin:admin@domain/path
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)
time.sleep(3)
driver.close()