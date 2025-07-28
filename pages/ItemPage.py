from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.src.locators import ItemPageLocators
from utils.logger import logger

class ItemPage(MainPage):

    def get_item_name(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.ITEM_NAME)
        )
        name = self.browser.find_element(*ItemPageLocators.ITEM_NAME)
        name = name.text
        logger.info(f"Получено имя товара: {name}")
        return name

    def get_item_price(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ItemPageLocators.ITEM_PRICE)
        )
        price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE)
        price = price.text
        logger.info(f"Получена цена товара: {price}")
        return price

    def add_item_to_cart(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ItemPageLocators.BTN_ADD)
            )
            btn = self.browser.find_element(*ItemPageLocators.BTN_ADD)
            logger.info(f"Добавляем товар в корзину")
            btn.click()
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(ItemPageLocators.BTN_ADD)
            )
            logger.info(f"Товар добавлен в корзину")
            return True
        
        except Exception as e:
            logger.warning(f"Товар не был добавлен в корзину! Message: {e}")
            return False
