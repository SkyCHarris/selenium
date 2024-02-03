
# Set up page object
# Each page on our website should be defined inside of a class
# Lots of selenium code

# Base class for all of our pages
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    # Does title of web page match what we want to match
    def is_title_matches(self):
        return "Python" in self.driver.title