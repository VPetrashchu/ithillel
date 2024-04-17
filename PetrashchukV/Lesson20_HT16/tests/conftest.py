import pytest
from selenium.webdriver import Chrome
from Lesson20.pages.dashboard_page import Dashboard
from Lesson20.pages.category_page import CategoryPage
from Lesson20.pages.search import Search


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver #return driver
    driver.quit()

@pytest.fixture()
def dashboard(driver):
    driver.get('https://horecacv.com.ua/')
    yield Dashboard(driver)


@pytest.fixture()
def dishes(driver):
    driver.get('https://horecacv.com.ua/ua/g108720607-posuda')
    yield CategoryPage(driver)

@pytest.fixture()
def search(driver):
    driver.get('https://horecacv.com.ua/')
    yield Search(driver)

@pytest.fixture()
def search_result(driver):
    driver.get('https://horecacv.com.ua/ua/site_search?search_term=%D0%A2%D0%B0%D1%80%D1%96%D0%BB%D0%BA%D0%B0')
    yield Search(driver)

