#Login

import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys('sdhawnicmr@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys('12345')
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()

    def test_login_with_invalid_email_valid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(generate_email_timestamp())
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('12345')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warnng_mgs)

    #generate a new invalid email id everytime
    def test_login_with_valid_email_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys('sdhawnicmr@gmail.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('12345987')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warnng_mgs)


    def test_login_without_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys('')
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('')
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_warnng_mgs = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_warnng_mgs)

    def generate_email_timestamp(self):
        time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sdhawnicmr"+time_stamp+'@gmail.com'

#**********SEARCH*********************
import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        self.driver.find_element(By.NAME, 'search').send_keys('HP')
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        time.sleep(2)
        print(self.driver.title)

    def test_serach_for_invalid_product(self):
        self.driver.find_element(By.NAME, 'search').send_keys('Honda')
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        time.sleep(2)
        print(self.driver.title)

    def test_search_without_any_product(self):
        self.driver.find_element(By.NAME, 'search').send_keys('')
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        time.sleep(2)
        print(self.driver.title)

#Fixtures
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

pytest.fixture(scope="function")
def setup_and_teardown(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    url = "https://tutorialsninja.com/demo/"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()