from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Create Chrome options object
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors

# Set up ChromeDriver path directly if 'service' is not supported
chrome_driver_path = ChromeDriverManager().install()

# Create the WebDriver instance with the driver path and options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.implicitly_wait(2)
driver.get("https://realpython.com/")

# Scroll to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# Take a screenshot and save it
driver.get_screenshot_as_file("screen2.png")
driver.quit()
