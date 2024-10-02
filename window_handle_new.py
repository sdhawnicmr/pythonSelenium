import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

# Store the ID of the main window
main_window = driver.current_window_handle

# Perform an action that opens a new window (e.g., clicking a link)
link = driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]")  # Modify as per your link
link.click()

# Wait for the new window to open
time.sleep(2)  # Wait time to ensure new window opens
print(driver.current_window_handle)
print("**************")
# Get the list of all open window handles
all_windows = driver.window_handles

# Switch to the newly opened window (usually the last one in the list)
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# Now you are in the new window, perform the desired actions
print(driver.title)  # Example action: Print the title of the new window

# After performing actions in the new window, switch back to the main window
driver.switch_to.window(main_window)
# Now you are back in the main window
print(driver.title)  # Example action: Print the title of the main window

# Continue your automation here
# Cleanup (close driver)
driver.quit()
