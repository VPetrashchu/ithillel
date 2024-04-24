from .base_locators import BaseLocators

class DashboardLocators(BaseLocators):
        locator_dishes = '//div[@class="b-product-groups-list__text-wrap"]//a[contains(text(), "Посуд")]'
        locator_discount = '//div[@class="b-menu__link-wrap"]//a[@href="/ua/discounted_products"] [not(data-qaid="menu_item")]'
        locator_first_product_of_discount = '//a[@id="link_to_product_635332903"]'
        locator_house_stuff = '//div[@class="b-product-groups-list__text-wrap"]//a[contains(text(), "Товари для дому")]'

