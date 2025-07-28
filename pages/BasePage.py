from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException,
    TimeoutException)
from pages.src.locators import ItemPageLocators
from utils.logger import logger

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        logger.info(f"Открываем url: {url}")
        self.browser.get(url)

    def open_item_page_by_url(self, url):
        logger.info(f"Открываем страницу товара: {url}")
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.PRODUCT_WRAP)
        )   

    def get_current_url(self):
        url = self.browser.current_url
        logger.info(f"Адрес открытой страницы: {url}")
        return url
    
    def get_status_code(self):
        for request in self.browser.requests:
            if request.response and request.url == \
                self.browser.current_url:
                        status_code = request.response.status_code
                        logger.info(f"Status code: {status_code}")
                        return status_code
            
    def is_not_empty(self):
          if self.browser.page_source.strip() != "":
               return True
          else: return False

    def check_element(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            logger.warning(f"Элемент не найден в DOM. Селектор элемента: {locator}")
            return False

        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            logger.warning(f"Элемент найден в DOM, но не виден за 10 секунд. Селектор элемента: {locator}")

    def scroll_to_element(self, element):
        try:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            logger.debug(f"Прокрутили к элементу {element}")
        except Exception as e:
             logger.error(f"Невозможно прокрутить к элементу {element}: {e}")