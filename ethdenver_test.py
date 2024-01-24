from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.ethdenver.com/")

link = driver.find_element(By.LINK_TEXT, "Book Your Lodging")
link.click()

time.sleep(10)  # waits for window 2 to load

driver.switch_to.window(driver.window_handles[1])   # switches operations to 2nd window

element = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.LINK_TEXT, "FAQ")))
element.click()

# driver.back()   # goes back to previous page (doesn't work with multiple windows?)
# driver.execute_script("window.history.go(-1)")    # also not working

time.sleep(10)  # keeps window open (anti auto-quit)