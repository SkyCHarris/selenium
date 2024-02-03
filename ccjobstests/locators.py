
# Any CSS Selector, ID, etc. should be in one location
# Create classes that represent objects we want to find

from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_BOX = (By.CLASS_NAME, "ais-SearchBox-input") # selects search box on mainpage

# Use classes inside locators to access those locators
class SearchResultsPageLocators(object):
    pass
