

class BaseLocators:
    locator_about_us = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/about_us"] [not(data-qaid="menu_item")]'
    locator_contacts = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/contacts"][not(data-qaid="menu_item")]'
    locator_discount_products = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/discounted_products"][not(data-qaid="menu_item")]'
    locator_articles = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/articles"][not(data-qaid="menu_item")]'
    locator_cart_items_counter = '//div[@class="b-cart-button__wrapper"]//span[@class="b-cart-button__counter js-shopping-cart-counter"]'
    locator_delivery_and_payment = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/delivery_info"][not(data-qaid="menu_item")]'
    locator_header_goods_services = '//a[@href="/ua/product_list"][not(data-qaid="menu_item")]/..'
    locator_sidebar_goods_services = '//div[@class="b-page__row"]//ul[@class="b-nav"]//span[@class="b-nav__arrow"]'
    locator_small_household_appliances = '//ul[@class="b-menu__sub-nav b-sub-menu"]//a[@href="/ua/g106455197-melkaya-bytovaya-tehnika"]'
