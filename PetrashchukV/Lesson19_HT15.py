from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_search():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get('https://rozetka.com.ua/')
    search_locator = '//input[@name="search"]'
    search_element = driver.find_element(by='xpath', value=search_locator) #by=By.XPATH
    search_element.send_keys('Планшет')
    search_element.send_keys(Keys.ENTER)
    time.sleep(5)
    first_non_ad_result_locator = '//section[@class="content content_type_catalog"]//div[1]//span[contains(text(), "ZAAM0190UA")]/..'
    first_element = driver.find_element('xpath', first_non_ad_result_locator)
    first_element.click()
    time.sleep(5)
    assert driver.current_url == 'https://rozetka.com.ua/ua/lenovo-zaam0190ua/p392003949/'
    driver.quit()

def test_actionchains():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://rozetka.com.ua/')
    search_locator = '//input[@name="search"]'
    search_element = driver.find_element(by='xpath', value=search_locator)
    search_element.send_keys('Планшет')
    actions = ActionChains(driver)
    time.sleep(2)
    actions.key_down(Keys.CONTROL).key_down('a').key_up(Keys.CONTROL).perform()
    time.sleep(5)
    actions.key_down(Keys.CONTROL).key_down('x').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    search_element.click()
    actions.key_down(Keys.CONTROL).key_down('v').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    driver.quit()


def test_pagination():
    driver = webdriver.Chrome()
    driver.get('https://rozetka.com.ua/ua/tablets/c130309/#search_text=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82%D0%B8')
    search_next_page = '//div[@class="pagination ng-star-inserted"]//a[contains(text(), "2")]/.'
    next_page = driver.find_element(by='xpath', value=search_next_page)
    actions = ActionChains(driver)
    actions.move_to_element(next_page).perform()
    actions.click()
    assert driver.current_url == 'https://rozetka.com.ua/ua/tablets/c130309/page=2/'
    driver.quit()

def test_filter_by_max_price():
    driver = webdriver.Chrome()
    driver.get('https://rozetka.com.ua/ua/tablets/c130309/#search_text=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82%D0%B8')
    search_max_item_locator = '//div[@data-goods-id="357750312"]//rz-button-product-page[2]//span/..'
    search_max_item = driver.find_element(by='xpath', value=search_max_item_locator)
    time.sleep(2)
    search_max_item.click()
    time.sleep(5)
    assert driver.current_url == 'https://rozetka.com.ua/ua/planshet-apple-ipad-pro-11-m2-wi-fi-1tb/g46867305/'
    driver.quit()

def test_filter_by_min_price():
    driver = webdriver.Chrome()
    driver.get('https://rozetka.com.ua/ua/tablets/c130309/#search_text=%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82%D0%B8')
    search_min_item_locator = '//div[@data-goods-id="414609816"]//rz-button-product-page[2]//span/..'
    search_min_item = driver.find_element(by='xpath', value=search_min_item_locator)
    time.sleep(2)
    search_min_item.click()
    time.sleep(5)
    assert driver.current_url == 'https://rozetka.com.ua/ua/teclast-6940709685907/p414609816/'
    driver.quit()



