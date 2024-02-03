
# Set up page object
# Each page on our website should be defined inside of a class
# Lots of selenium code

from element import BasePageElement
from locators import MainPageLocators

# Element on page we want to access
class SearchTextElement(BasePageElement):
    locator = "q"

class SearchBarElement(BasePageElement):
    locator = "go"

# Base class for all of our pages
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    # Descriptor. Hide functionality of certain attr.
    search_text_element = SearchTextElement()

    # Does title of web page match what we want to match
    def is_title_matches(self):
        return "Cryptocurrency Jobs" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)    # * = unpack, splat
        element.click()

# Tells if results are found from source page
class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source