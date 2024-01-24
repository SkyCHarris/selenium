from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("https://cryptocurrencyjobs.co/?query=marketing")

# waits for page to load, waits for all elements to be located, selects elements by CLASS_NAME, 'ais-Hits-item'
jobs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ais-Hits-item')))

# prints marketing job results with diff. info needed (part/full, company, job title, etc.)
for job in jobs:
    print(job.text)
