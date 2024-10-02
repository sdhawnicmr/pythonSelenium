from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--private")

driver = webdriver.Firefox(options=firefox_options)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(3)

driver.close()
