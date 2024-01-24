#! Locating Elements from HTML

# How to access elements on the page
# Acess via differently properties:
# -Name
# -ID
# -Class
# -etc.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# get request to landing page
driver.get("https://cryptocurrencyjobs.co/")

# get search bar element
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-SearchBox-input')))

# auto-input "test" in search bar
search.send_keys("marketing")

# auto-hit return
search.send_keys(Keys.RETURN)

#* Bring in search results, access titles

time.sleep(5)

# grab jobs via wrapper div class 'ais-Hits', print text within

try:
    jobs_wrapper = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-Hits')))
    # print(jobs_wrapper.text)

    positions = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'h2')))
    for position in positions:
        print(position.text)

finally:
    driver.quit()
    
