
#! Action Chains & Automating Cookie Clicker

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

# driver.refresh()
driver.implicitly_wait(5)

# web_cookies = driver.find_element(By.TAG_NAME, "a")
# web_cookies.click()

driver.implicitly_wait(5)

#TODO: Issue must be with the elements below
cookie = driver.find_element(By.ID, "bigCookie")
# cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
cookie_count = driver.find_element(By.ID, "cookies")    #TODO: is this getting in the way?
# cookie_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookies")))

# load in all elements with id productPrice, + str(i) in for loop (upgrades more expensive items first)
# items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]


for i in range(5000):
    actions = ActionChains(driver)  # actionchains object, works like a queue
    actions.perform()   # performs above actions (click cookie)
    actions.click(cookie) # click mouse wherever it's located

time.sleep(10)
