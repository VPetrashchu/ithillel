
import pytest
from PetrashchukV.Lesson22_HT18.pages.product_page import Product
from PetrashchukV.Lesson22_HT18.core.datesample import product_id

def test_buy_to_glass_from_discount(dashboard):
    discount_category = dashboard.click_discount()
    glass_product = discount_category.click_first_product_of_discount()
    assert glass_product.driver.current_url == 'https://horecacv.com.ua/ua/p635332903-bolshoj-vysokij-stakan.html'

def test_product_added_to_cart_origin_way(large_tall_glass):
    large_tall_glass.click_buy_origin()
    assert large_tall_glass.return_cart_counter() == 1

def test_product_added_to_cart_prom_way(large_tall_glass):
    large_tall_glass.click_buy_prom()
    assert large_tall_glass.return_cart_counter() == 1

@pytest.mark.parametrize('product_id', [(product_id)
])
def test_large_tall_glass(large_tall_glass, driver, product_id):
    url = f'https://horecacv.com.ua/ua/p{product_id}.html'
    driver.get(url)
    assert Product(driver)