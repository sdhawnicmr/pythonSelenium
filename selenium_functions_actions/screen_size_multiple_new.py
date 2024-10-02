import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

viewport = [(1024,768),(768,1024),(375, 667)]
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://realpython.com/"
driver.get(url)
try:
    for width, height in viewport:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()
