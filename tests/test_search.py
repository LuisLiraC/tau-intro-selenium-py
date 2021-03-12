"""
These test cover Google searches
"""

import pytest
from pages.result import GoogleResultPage
from pages.search import GoogleSearchPage

@pytest.mark.parametrize('phrase', ['nintendo', 'xbox', 'steam'])
def test_basic_google_search(browser, phrase):
    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)

    search_page.load()
    search_page.search(phrase)

    assert phrase == result_page.search_input_value()

    # for title in result_page.result_link_titles():
    #     assert phrase.lower() in title.lower()

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    assert phrase in result_page.title()
