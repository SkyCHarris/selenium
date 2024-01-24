
#! Selenium Tutorial #1: Web Scraping, Bots, Testing

# Framework allowing us to interact with html elements from any website
# Interact with those elements
    # Bots, automated script

# -Drag and drop
# -Click button
# -Fill in form
# -Enter in search field
# -Grab data from tags
# -Find elements in source code
# -Read entire source code

from selenium import webdriver
# PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
# need path to file so we can run it
driver = webdriver.Chrome()

driver.get("https://cryptocurrencyjobs.co/?query=marketing")
print(driver.title) # print driver title