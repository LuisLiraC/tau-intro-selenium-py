"""
This modulea contains GoogleSearchPage,
the page object for the Google search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:

    URL = 'https://www.google.com.mx/'
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # search_input.send_keys(phrase + Keys.RETURN)
        search_input.send_keys(phrase)
        search_input.submit()
