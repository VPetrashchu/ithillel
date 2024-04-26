from PetrashchukV.Lesson22_HT18.pages.category_page import CategoryPage
from PetrashchukV.Lesson22_HT18.core.locators.base_locators import BaseLocators
from PetrashchukV.Lesson22_HT18.pages.dashboard_page import Dashboard
from PetrashchukV.Lesson22_HT18.core.datesample import header_goods_services_list,sidebar_goods_services_list
import time
import pytest

def test_do_to_dishes_and_check(dashboard):
    category = dashboard.click_dishes()
    category.click_checkbox_dessert()
    category.click_first_product()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/g108720607-posuda'


def test_go_to_about_us(dashboard):
    dashboard.click_header_about_us()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/about_us'

def test_contacts(dashboard):
    dashboard.click_header_contacts()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/contacts'

def test_articles(dashboard):
    dashboard.click_header_locator_articles()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/articles'

def test_go_to_delivery_and_payment(dashboard):
    dashboard.click_header_delivery_and_payment()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/delivery_info'

def test_go_to_discount(discount):
    discount.click_discount()
    assert discount.driver.current_url == 'https://horecacv.com.ua/ua/discounted_products'

def test_go_to_discount_and_check_product(dashboard):
    category = dashboard.click_header_discount()
    product = category.click_first_product_of_discount()

def test_do_to_house_stuff_and_check(dashboard):
    category = dashboard.click_house_stuff()
    category.click_checkbox_producing_country()
    category.click_first_house_stuff_by_spain()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/p1651478406-elastichnoe-rezinovoe-hozyajstvennoe.html'

def test_opening_condition_popup(plastic_bucket):
    plastic_bucket.click_more_icon_of_bucket()
    assert plastic_bucket.click_opening_condition_popup() == 'Умови повернення та обміну'


def test_close_condition_popup(plastic_bucket):
    category = plastic_bucket.click_more_icon_of_bucket()
    category.click_close_condition_popup()
    assert category.return_close_popup(), "Popup did not close"

@pytest.mark.parametrize('category,list_of_subcategories', [
    (BaseLocators.locator_header_goods_services,header_goods_services_list),
    (BaseLocators.locator_sidebar_goods_services,sidebar_goods_services_list)
])
def test_navigate_to_goods_services(dashboard,category,list_of_subcategories):
    assert dashboard.navigate_to_category(category, list_of_subcategories)
    time.sleep(5)


@pytest.mark.parametrize('section, expected_url', [
    ('about_us', 'https://horecacv.com.ua/ua/about_us'),
    ('contacts', 'https://horecacv.com.ua/ua/contacts'),
    ('articles', 'https://horecacv.com.ua/ua/articles'),
    ('delivery_and_payment', 'https://horecacv.com.ua/ua/delivery_info')
])
def test_navigation_from_dashboard(dashboard, section, expected_url):
    if section == 'delivery_and_payment':
        dashboard.click_header_delivery_and_payment()
    elif section == 'articles':
        dashboard.click_header_locator_articles()
    else:
        getattr(dashboard, f'click_header_{section}')()

    assert dashboard.driver.current_url == expected_url






