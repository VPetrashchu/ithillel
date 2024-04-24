from PetrashchukV.Lesson20_21.pages.base_page import BasePage
from PetrashchukV.Lesson20_21.pages.product_page import Product
from PetrashchukV.Lesson20_21.core import CategoryLocators

class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()



    def click_first_product(self):
        self.click_on_element(self.locators.locator_first_product_by_me)

    def click_checkbox_dessert(self):
        self.click_on_element(self.locators.locator_checkbox_dessert)

    def click_header_discount(self):
        self.click_on_element(self.locators.locator_discount)


    def click_first_product_of_discount(self):
        self.click_on_element(self.locators.locator_first_product_of_discount)
        return Product(self.driver)

    def click_checkbox_producing_country(self):
        self.click_on_element(self.locators.locator_checkbox_producing_country)

    def click_first_house_stuff_by_spain(self):
        self.click_on_element(self.locators.locator_house_stuff_producing_by_spain)

    def click_more_icon_of_bucket(self):
        self.click_on_element(self.locators.locator_more_icon_of_bucket)
        return self

    def click_opening_condition_popup(self):
        appear_popup = self.wait_until_element_presence(self.locators.locator_checking_condition_return)
        return appear_popup.text

    def click_close_condition_popup(self):
        self.click_on_element(self.locators.locator_close_condition_popup)

    def return_close_popup(self):
        return self.wait_for_popup_to_close(self.locators.locator_close_condition_popup)