import pytest
from selenium.webdriver import Chrome
from PetrashchukV.Lesson22_HT18.pages.dashboard_page import Dashboard
from PetrashchukV.Lesson22_HT18.pages.category_page import CategoryPage
from PetrashchukV.Lesson22_HT18.pages.search import Search
from PetrashchukV.Lesson22_HT18.pages.product_page import Product



@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    print(f"Cookies:{driver.get_cookies()}")
    yield driver #return driver
    driver.quit()

@pytest.fixture()
def dashboard(driver):
    driver.get('https://horecacv.com.ua/ua/')
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

@pytest.fixture()
def discount(driver):
    driver.get('https://horecacv.com.ua/ua/discounted_products')
    yield Dashboard(driver)

@pytest.fixture()
def large_tall_glass(driver):
    driver.get('https://horecacv.com.ua/ua/p635332903-bolshoj-vysokij-stakan.html')
    print(f"Cookies:{driver.get_cookies()}")
    print(f"Cookies:{driver.add_cookie({'name':'mysterious_cookie','value':'mysterious_value'})}")
    print(f"Cookies:{driver.add_cookie({'name':'mysterious_cookie','value':'mysterious_value'})}")
    yield Product(driver)

@pytest.fixture()
def plastic_bucket(driver):
    driver.get('https://horecacv.com.ua/ua/p1651478406-elastichnoe-rezinovoe-hozyajstvennoe.html')
    yield CategoryPage(driver)



