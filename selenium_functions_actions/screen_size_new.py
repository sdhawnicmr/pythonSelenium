import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://realpython.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.set_window_size(768, 1024)
time.sleep(5)
driver.close()

