from Lesson20.pages.base_page import BasePage

class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator_dishes = ('xpath', '//div[@class="b-product-groups-list__text-wrap"]//a[contains(text(), "Посуд")]')


    def click_dishes(self):
        self.click_on_element(self.locator_dishes)