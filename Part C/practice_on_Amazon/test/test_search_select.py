import pytest
from time import sleep
from practice_on_Amazon.Pages.search_page import SearchPage
from practice_on_Amazon.Pages.select_page import SelectPage

def test_amazon(setup_and_teardown):

    search = SearchPage(setup_and_teardown)
    select = SelectPage(setup_and_teardown)
    search.search_product('perfume')
    sleep(2)
    select.select_sort_option('Price: Low to High')
