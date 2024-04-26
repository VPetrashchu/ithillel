import time
from PetrashchukV.Lesson22_HT18.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PetrashchukV.Lesson22_HT18.core.locators.search_locators import SearchLocators


class Search(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locators = SearchLocators

    def find_search(self, search_term):
        search_box = self.driver.find_element(*self.locators.locator_search)
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)


    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def click_on_first_item(self):
        self.click_on_element(self.locators.locator_first_item)


