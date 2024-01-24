from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://cryptocurrencyjobs.co/")


WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, '//*[@id="hits"]/div/div/ol/li[1]/div/div[1]/h2')))
driver.switch_to.active_element  # circumvents cookies pop-up layer
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hits"]/div/div/ol/li[1]/div/div[1]/h2/a'))).click()

time.sleep(10)

#TODO: https://www.testim.io/blog/selenium-element-is-not-clickable-at-point/