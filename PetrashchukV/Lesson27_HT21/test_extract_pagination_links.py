import os
import json
from PetrashchukV.Lesson27_HT21.crawler import extract_pagination_links, return_links


def test_extract_pagination_links():
    class MockSoup:
        def find(self, *args, **kwargs):
            return MockPaginationSection()

    class MockPaginationSection:
        def find_all(self, *args, **kwargs):
            return [MockLink()]

    class MockLink:
        def get(self, attribute):
            return "page1"
    soup = MockSoup()
    pagination_links = extract_pagination_links(soup)
    assert pagination_links == ['page1']


def test_link_in_return_links():
    url = 'https://pethouse.ua/ua/shop/sobakam/suhoi-korm'
    links = return_links(url)
    expected_link = 'https://pethouse.ua/ua/shop/sobakam/suhoi-korm/josera/josera-josidog-ekonomy-228/'
    assert expected_link in links

def test_empty_file(tmp_path):
    file_path = tmp_path / "empty_file.txt"
    open(file_path, 'a').close()
    assert os.path.exists(file_path), f"Файл {file_path} не існує"
    with open(file_path, 'r') as file:
        content = file.read()
        assert content == "", f"Файл {file_path} містить дані: {content}"


def test_suhoi_korm_json_not_empty():
    file_path = 'suhoi-korm_page_1.json'
    assert os.path.exists(file_path), f"Файл {file_path} не існує"
    with open(file_path, 'r') as file:
        data = json.load(file)
    assert data, f"Файл {file_path} порожній"


def test_return_links_missing_json():
    file_path = 'nonexistent.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            expected_links = json.load(file)
    else:
        expected_links = []
    actual_links = return_links('https://pethouse.ua/ua/shop/sobakam/suhoi-korm')
    assert actual_links == expected_links, "Expected links do not match actual links"