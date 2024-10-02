import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
url= "https://www.globalsqa.com/demo-site/datepicker/"

driver.get(url)
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "close_img").click()
time.sleep(1)
#switch to iframe
iframe= driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(iframe)
time.sleep(1)
#locator for clicking on calender two ways
#driver.find_element(By.CSS_SELECTOR, "input[id='datepicker']").click()
#time.sleep(1)
date_picker= driver.find_element(By.CSS_SELECTOR, "#datepicker")
time.sleep(1)
#current date
current_date= datetime.now()
#past date
last_date = current_date+timedelta(days=-1)  #current date -1, last day
#future date
next_date = current_date+timedelta(days=5) #current date+5, 5th day from now
#time format
formatted_date = next_date.strftime("%m/%d/%y")
date_picker.send_keys(formatted_date + Keys.TAB)

time.sleep(2)

#if date type is text, we can simply copy the selected date and proceed further

driver.quit()

