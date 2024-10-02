import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
driver.get(url)
#identify the corner from where it can be dragged

resizable_ele = driver.find_element(By.XPATH, "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_box_size = driver.find_element(By.XPATH,"//div[@id='resizable']")
initial_size = initial_box_size.size
print(initial_size)

actions = ActionChains(driver)
actions.click_and_hold(resizable_ele).move_by_offset(100,100).release().perform()
resized_ele= initial_box_size.size
print(resized_ele)

driver.close()
