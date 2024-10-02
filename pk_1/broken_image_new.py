import requests
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = "https://the-internet.herokuapp.com/broken_images"

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.maximize_window()

#find broken images
images = driver.find_elements(By.TAG_NAME,'img')
broken_image = []

for img in images:
    src = img.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code!= 200:
            broken_image.append(src)
            print("Broken Image found")
if broken_image:
    print("list of broken images")
    for broken_img in broken_image:
        print(broken_image)
else:
    print("No Broken Image")

driver.close()
