
#! Scrape Dynamic Websites with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


import pandas as pd         #to save CSV file
from bs4 import BeautifulSoup
url = "https://crypto.jobs/jobs?search=marketing&location=Remote"

driver = webdriver.Chrome()

driver.get(url)

# implicit wait
element = driver.find_elements(By.CLASS_NAME, "li")
time.sleep(7)
element.click()
driver.implicitly_wait(20)

# parse with BeautifulSoup
result = driver.page_source
soup = BeautifulSoup(result, 'html.parser')
page = list(soup.find_all('tr', class_="job_entry"))

print(page)



# jobs = driver.find_elements(By.CLASS_NAME, "li")
# print(jobs)

# # for job in jobs:
# #     print(job)