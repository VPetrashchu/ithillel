from .base_locators import BaseLocators

class CategoryLocators(BaseLocators):
        locator_about_us = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/about_us"] [not(data-qaid="menu_item")]'
        locator_first_product_by_google = '/html/body/div[9]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[1]/a'
        locator_first_product_by_me = '//ul[@class="b-product-groups-list"]//a[contains(text(), "Посуд кухонний")]'
        locator_checkbox_dessert = '//ul[@id="csbss4_list"]//span[contains(text(), "Десертні")]/..'
        locator_discount = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/discounted_products"] [not(data-qaid="menu_item")]'
        locator_first_product_of_discount = '//a[@id="link_to_product_635332903"]'
        locator_checkbox_producing_country = '//div[@class="b-filter__wrapper"]//span[contains(text(), "Іспанія")]/..'
        locator_house_stuff_producing_by_spain = '//div[@class="b-product-gallery__inf-wrap"]//a[@id="link_to_product_1651478406"]'
        locator_more_icon_of_bucket = '//div[@class="b-product__info-line"]//div[contains(text(), "Детальніше")]'
        locator_checking_condition_return = '//div[@class="ROverlay__overlay--3VJkJ"]//h4[contains(text(), "Умови повернення та обміну")]'
        locator_close_condition_popup = '//div[@class="ROverlay__overlay--3VJkJ"]//button[@aria-label="close_btn"]'
