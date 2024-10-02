import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--window-size=768,1024")  # Set window size

# Create a Chrome driver with options
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

url = "https://realpython.com/"
driver.get(url)
print("--headless mode---")
time.sleep(5)
driver.close()
print("--headless mode---")
