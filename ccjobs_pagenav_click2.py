from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://cryptocurrencyjobs.co/")


# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hits"]/div/div/ol/li[1]/div/div[1]/h2[@title='Accept & Close']'))).click()
# driver.switch_to.active_element  # circumvents cookies pop-up layer
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="hover:text-purple transition-colors"]'))).click()

time.sleep(10)

#TODO: https://www.testim.io/blog/selenium-element-is-not-clickable-at-point/
