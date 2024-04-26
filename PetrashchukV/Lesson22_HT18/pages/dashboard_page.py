from PetrashchukV.Lesson22_HT18.pages.base_page import BasePage
from PetrashchukV.Lesson22_HT18.pages.category_page import CategoryPage
from PetrashchukV.Lesson22_HT18.pages.product_page import Product
from PetrashchukV.Lesson22_HT18.core import DashboardLocators


class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()


    def click_dishes(self):
        self.click_on_element(self.locators.locator_dishes)

    def click_discount(self):
        self.click_on_element(self.locators.locator_discount)
        return CategoryPage(self.driver)

    def click_first_product_of_discount(self):
        self.click_on_element(self.locators.locator_first_product_of_discount)

    def click_house_stuff(self):
        self.click_on_element(self.locators.locator_house_stuff)
        return CategoryPage(self.driver)
