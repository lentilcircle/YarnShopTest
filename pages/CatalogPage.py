from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.src.locators import ItemCardLocators, ItemPageLocators
from utils.logger import logger


class CatalogPage(MainPage):

    def open_first_item_page(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(ItemCardLocators.ITEM_CARD_PIC)
            )
            logger.debug("Ссылка на товар найдена. Открываем страницу товара")
            btn = self.browser.find_element(*ItemCardLocators.ITEM_CARD_PIC)
            self.scroll_to_element(btn)
            btn.click()
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(ItemPageLocators.PRODUCT_WRAP)
            )
            logger.info("Страница товара открыта")
            return True

        except Exception as e:
            logger.error(f"Ошибка при открытии страницы товара: {e}")
            return False
