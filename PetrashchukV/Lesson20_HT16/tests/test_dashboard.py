

def test_do_to_dishes(dashboard):
    dashboard.click_dishes()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/g108720607-posuda'


def test_go_to_about_us(dashboard):
    dashboard.click_header_about_us()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/about_us'

def test_contacts(dashboard):
    dashboard.click_header_contacts()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/contacts'

def test_discount_products(dashboard):
    dashboard.click_header_discount_products()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/discounted_products'

def test_discount_products(dashboard):
    dashboard.click_header_locator_articles()
    assert dashboard.driver.current_url == 'https://horecacv.com.ua/ua/articles'




