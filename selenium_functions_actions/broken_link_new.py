import requests
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://realpython.com/")

all_links= driver.find_elements(By.TAG_NAME, "a")
print(f"Total links in the webpage is {len(all_links)}")
#find href

for link in all_links:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >= 400:
        print(f" Broken link: {href} (status code: {response.status_code})")

driver.quit()