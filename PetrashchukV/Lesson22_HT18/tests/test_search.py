import pytest

def test_do_search(search):
    search.find_search()
    assert search.driver.current_url == 'https://horecacv.com.ua/ua/site_search?search_term=%D0%A2%D0%B0%D1%80%D1%96%D0%BB%D0%BA%D0%B0'

def test_open_first_item(search_result):
    search_result.click_on_first_item()
    assert search_result.driver.current_url == 'https://horecacv.com.ua/ua/p699157925-salfetka-set-pod.html'

@pytest.mark.parametrize('search_term', [
    ("Тарілка"),
    ("Кружка"),
    ("Ніж")
])
def test_search_functionality(search, search_term):
    search.find_search(search_term)
    expected_url_prefix = 'https://horecacv.com.ua/ua/site_search?search_term='
    assert search.driver.current_url.startswith(expected_url_prefix)
