import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = "https://www.google.com/"

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()
driver.execute_script("window.open('');")

time.sleep(2)
windows = driver.window_handles
print(len(windows))
print(windows)

current_window= driver.current_window_handle
print(current_window)
driver.quit()