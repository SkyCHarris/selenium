import unittest
from selenium import webdriver
import page

# Test must start with 'def test'

# Main test case to perform on this website
# Gives return information for test pass/fail
class PythonOrgSearchTest(unittest.TestCase):

    # Driver, url at beginning
    def setUp(self):
        print("setup")  # print to cli to see both setUps, called everytime tests are run
        self.driver = webdriver.Chrome()    # gets driver
        self.driver.get("https://www.python.org/")

    def test_example(self):
        print("test")
        assert True

    def test_example_2(self):
        assert False

    def not_a_test(self):
        print("this won't print")

    # Cleans up afterwards
    def tearDown(self):
        self.driver.close()

# Run all the unit tests we've defined
if __name__ == "__main__":
    unittest.main()