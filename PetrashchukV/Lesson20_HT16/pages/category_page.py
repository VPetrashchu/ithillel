from Lesson20.pages.base_page import BasePage

class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.web_driver_wait = WebDriverWait(driver, wait_time)
        self.locator_about_us = ('xpath', '//div[@class="b-menu__link-wrap"]//a[@href="/ua/about_us"] [not(data-qaid="menu_item")]')

        self.locator_first_product_by_google = ('xpath', '/html/body/div[9]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[1]/a')
        self.locator_first_product_by_me = ('xpath', '//ul[@class="b-product-groups-list"]//a[contains(text(), "Посуд кухонний")]')
        self.locator_checkbox_dessert = ('xpath', '//ul[@id="csbss4_list"]//span[contains(text(), "Десертні")]/..')



    def click_first_product(self):
        self.click_on_element(self.locator_first_product_by_me)

    def click_checkbox_dessert(self):
        self.click_on_element(self.locator_checkbox_dessert)

