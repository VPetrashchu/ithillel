from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locator_about_us = ('xpath', '//div[@class="b-menu__link-wrap"]//a[@href="/ua/about_us"] [not(data-qaid="menu_item")]')
        self.locator_contacts = ('xpath', '//div[@class="b-menu__link-wrap"]//a[@href="/ua/contacts"][not(data-qaid="menu_item")]')
        self.locator_discount_products = ('xpath', '//div[@class="b-menu__link-wrap"]//a[@href="/ua/discounted_products"][not(data-qaid="menu_item")]')
        self.locator_articles = ('xpath', '//div[@class="b-menu__link-wrap"]//a[@href="/ua/articles"][not(data-qaid="menu_item")]')

    def wait_until_element_presence(self, locator:tuple):
       return self.web_driver_wait.until(EC.presence_of_element_located(locator))


    def click_on_element(self, locator):
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_about_us(self):
        self.click_on_element(self.locator_about_us)

    def click_header_contacts(self):
        self.click_on_element(self.locator_contacts)

    def click_header_discount_products(self):
        self.click_on_element(self.locator_discount_products)

    def click_header_locator_articles(self):
        self.click_on_element(self.locator_articles)