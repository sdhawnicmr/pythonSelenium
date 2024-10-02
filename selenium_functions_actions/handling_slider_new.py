import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "https://the-internet.herokuapp.com/horizontal_slider"
driver.get(url)

slider = driver.find_element(By.XPATH,"//input[@type='range']")
time.sleep(1)
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(50,0).release().perform()

time.sleep(2)
driver.close()