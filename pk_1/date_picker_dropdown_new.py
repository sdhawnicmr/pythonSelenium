import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.find_element(By.XPATH,"//input[@id= 'datepicker2']").click()
time.sleep(1)

current_date = datetime.now()
print(current_date)

next_date = current_date + timedelta(days=1)
print(next_date)

Next_day = (str(next_date.day))
print(Next_day)

current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1  # selecting current month +2 = sept+2= nov
next_month_year = f"{next_month}/{current_year}"

#handle dropdown
month_dd = driver.find_element(By.CSS_SELECTOR, "select[title= 'Change the month']")
select = Select(month_dd)
select.select_by_value(str(next_month_year))

year_dd = driver.find_element(By.CSS_SELECTOR, "select[title= 'Change the year']")
select = Select(year_dd)
select.select_by_visible_text("2024")

driver.find_element(By.LINK_TEXT, Next_day).click()
time.sleep(2)
driver.quit()
