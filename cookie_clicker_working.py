from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

choose_lang = driver.find_element(By.ID, "langSelect-EN" )
choose_lang.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)  # actionchains object, works like a queue

for i in range(5000):
    actions.perform()   # performs above actions (click cookie)
    actions.click(cookie) # click mouse wherever it's located

#TODO: FKIN WORKS LEZZZ GOOOOO
