import unittest
from selenium import webdriver
import page

# Main test case to perform on this website
# Gives return information for test pass/fail
class PythonOrgSearchTest(unittest.TestCase):

    # Driver, url at beginning
    def setUp(self):
        print("setup")  # print to cli to see both setUps, called everytime tests are run
        self.driver = webdriver.Chrome()    # gets driver
        self.driver.get("https://cryptocurrencyjobs.co/")

    def test_search_ccjobs(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "marketing"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # Cleans up afterwards
    def tearDown(self):
        self.driver.close()