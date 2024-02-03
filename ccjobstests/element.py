
# Represent one element on the page
    # Search bar, form input, etc.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# When we have element on page, if we want to set its value, need to follow this process
    # driver -> webdriverwait (max 100sec) -> until function = true
    # function ->
    # self.locator = name we want to use to locate the element

class BasePageElement(object):
    locator = "q"

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.Name, self.locator))
        driver.find_element(By.NAME, self.locator).clear().send_keys(value)
    
    # Get value of object, don't worry about waiting anymore!
    # If we want to access the value of an element:
        # wait for element to exist -> element = find_element -> element.get_attribute value
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.Name, self.locator))
        element = driver.find_element(By.Name, self.locator)
        return element.get_attribute("value")
