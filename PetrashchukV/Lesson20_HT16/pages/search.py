import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Search():

    def __init__(self, driver):
        self.driver = driver
        self.locator_search = ('xpath', '//input[@id="search_term"]')
        self.locator_first_item = ('xpath', '//div[@class="b-product-gallery__inf-wrap"]//a[@href="/ua/p699157925-salfetka-set-pod.html"]')


    def find_search(self):
        search_box = self.driver.find_element(*self.locator_search)
        search_box.send_keys('Тарілка')
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def click_on_first_item(self):
        self.click_on_element(self.locator_first_item)
