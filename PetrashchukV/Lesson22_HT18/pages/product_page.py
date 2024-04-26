from PetrashchukV.Lesson22_HT18.pages.base_page import BasePage
from PetrashchukV.Lesson22_HT18.core import ProductLocators

class Product(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()


    def click_buy_origin(self):
        self.click_on_element(self.locators.locator_button_buy_origin)

    def click_buy_prom(self):
        self.click_on_element(self.locators.locator_button_buy_prom)

