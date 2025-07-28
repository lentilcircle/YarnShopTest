from selenium.common.exceptions import (NoSuchElementException,
    ElementClickInterceptedException, TimeoutException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from pages.src.locators import BasePageLocators, CartLocators
from pages.src.urls import Pages
from utils.logger import logger

class MainPage(BasePage):

    def open_catalog(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(BasePageLocators.BH_BTN_PRYAZA_CATALOG)
            )
            btn = self.browser.find_element(*BasePageLocators.BH_BTN_PRYAZA_CATALOG)
            logger.debug(f"Кнопка каталога найдена. Пытаемся открыть каталог")
            btn.click()
            WebDriverWait(self.browser, 10).until(
                EC.url_contains('/catalog/')
            )
            logger.info(f"Каталог открыт")
            return self.browser.current_url

        except NoSuchElementException as e:
            logger.error(f"Кнопка открытия каталога не найдена: {e}")

        except ElementClickInterceptedException as e:
            logger.warning(f"Клик по кнопке открытия каталога не удался (перекрыта?): {e}")

        except Exception as e:
            logger.error(f"Неизвестная ошибка при открытии каталога: {e}")


    def open_search(self):
        popup_opened = False
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(BasePageLocators.BH_BTN_SEARCH)
            )
            btn = self.browser.find_element(*BasePageLocators.BH_BTN_SEARCH)
            logger.debug(f"Кнопка поиска найдена. Пытаемся открыть поиск")
            btn.click()
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(BasePageLocators.SEARCH_POPUP_ACTIVE)
            )
            popup_opened = True
            logger.debug(f"Появилось активное окно поиска")
            logger.info(f"Поиск открыт")

        except ElementClickInterceptedException as e:
            logger.warning(f"Клик по кнопке поиска не удался (перекрыта?): {e}")

        except Exception as e:
            logger.error(f"Ошибка при открытии поиска: {e}")

        finally:
            if popup_opened:
                try:
                    logger.info(f"Закрываем окно поиска")
                    WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable(BasePageLocators.SEARCH_BTN_CLOSE)
                    )
                    btn = self.browser.find_element(*BasePageLocators.SEARCH_BTN_CLOSE)
                    logger.debug(f"Кнопка закрытия поиска найдена. Пытаемся закрыть поиск")
                    btn.click()
                    WebDriverWait(self.browser, 10).until(
                        EC.invisibility_of_element_located(BasePageLocators.SEARCH_POPUP_ACTIVE)
                    )
                    logger.info(f"Окно поиска закрыто")
                except Exception as e:
                    logger.error(f"Ошибка при закрытии поиска: {e}")


 
    def open_cart(self):
        logger.debug(f"Пытаемся открыть корзину")

        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(BasePageLocators.BH_BTN_CART)
            )
            btn = self.browser.find_element(*BasePageLocators.BH_BTN_CART)
            btn.click()
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(CartLocators.CART_BODY)
            )
            logger.info(f"Корзина открыта")
            return True

        except TimeoutException as e:
            logger.warning(f"Кнопка открытия корзины не стала кликабельной за 10 секунд: {e}")
            return False

        except NoSuchElementException as e:
            logger.error(f"Кнопка открытия корзины не найдена: {e}")
            return False
        
        except ElementClickInterceptedException as e:
            logger.warning(f"Клик по кнопке открытия не удался (перекрыта?): {e}")
            return False
        
        except Exception as e:
            logger.error(f"Неизвестная ошибка при открытии корзины: {e}")
            return False

