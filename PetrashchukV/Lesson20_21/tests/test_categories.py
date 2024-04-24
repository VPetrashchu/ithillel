

def test_first_product(dishes):
    dishes.click_first_product()
    assert dishes.driver.current_url == 'https://horecacv.com.ua/ua/g108720622-posuda-kuhonnaya'

def test_checkbox_and_first_product(dishes):
    dishes.click_first_product()
    dishes.click_checkbox_dessert()
    assert dishes.driver.current_url == 'https://horecacv.com.ua/ua/g108720622-posuda-kuhonnaya?csbss4=706521854'

