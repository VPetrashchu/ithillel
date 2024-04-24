from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PetrashchukV.Lesson20_21.core import BaseLocators

class BasePage:

    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locators = BaseLocators()

    def by_locator(self, locator, locator_type='xpath'):
        return (locator_type, locator)

    def wait_until_element_presence(self, locator:tuple, locator_type='xpath'):
       return self.web_driver_wait.until(EC.presence_of_element_located(self.by_locator(locator)))

    def wait_for_popup_to_close(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(self.by_locator(locator)))
            return True
        except TimeoutException:
            return False

    def click_on_element(self, locator, scroll=False):
        if scroll:
            self.scroll_a_bit()
        element = self.wait_until_element_presence(locator)
        element.click()

    def click_header_about_us(self):
        self.click_on_element(self.locators.locator_about_us)


    def click_header_delivery_and_payment(self):
        self.click_on_element(self.locators.locator_delivery_and_payment)

    def click_header_contacts(self):
        self.click_on_element(self.locators.locator_contacts)

    def click_header_discount_products(self):
        self.click_on_element(self.locators.locator_discount_products)

    def click_header_locator_articles(self):
        self.click_on_element(self.locators.locator_articles)

    def return_cart_counter(self):
        cart_counter = self.wait_until_element_presence(self.locators.locator_cart_items_counter)
        return int(cart_counter.text)


