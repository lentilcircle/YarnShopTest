from time import sleep
from selenium.common.exceptions import (
    StaleElementReferenceException, ElementClickInterceptedException,
    )
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.BasePage import BasePage
from pages.src.locators import CartLocators, CheckoutPageLocators
from utils.logger import logger


class CartModal(BasePage):

    def get_items_names(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(CartLocators.ITEM_NAMES_IN_CART)
            )
            items_list = self.browser.find_elements(*CartLocators.ITEM_NAMES_IN_CART)
            items_names = [item.text for item in items_list]
            logger.info(f"Получены названия товаров в корзине: {items_names}")
            return items_names
        except:
            logger.warning(f"Названия товаров в корзине не получены")


    def get_items_prices(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(CartLocators.ITEM_PRICES_IN_CART)
        )
        items_list = self.browser.find_elements(*CartLocators.ITEM_PRICES_IN_CART)
        items_prices = [item.text for item in items_list]
        logger.info(f"Получены цены товаров в корзине: {items_prices}")
        return items_prices

    def get_items_costs(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(CartLocators.ITEM_COSTS)
        )
        items_list = self.browser.find_elements(*CartLocators.ITEM_COSTS)
        items_costs = [item.text for item in items_list]
        logger.info(f"Получены стоимости товаров в корзине: {items_costs}")
        return items_costs

    def close_cart(self):
        logger.info("Пытаемся закрыть корзину")

        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(CartLocators.BTN_CLOSE)
            )
            btn = self.browser.find_element(*CartLocators.BTN_CLOSE)
            btn.click()
            WebDriverWait(self.browser, 10).until_not(
                EC.visibility_of_element_located(CartLocators.CART_BODY)
            )
            logger.info("Корзина закрыта")

        except Exception as e:
            logger.error(f"Ошибка при закрытии корзины: {e}")

    def get_total_without_discount(self):
        pass

    def delete_item(self):
        pass

    def clear_cart(self):
        removed = 0
        repeat_counter = 5
        max_stuck_repeats = 10

        while True:
            WebDriverWait(self.browser, 10).until(
                lambda browser: (
                browser.find_elements(*CartLocators.BTN_ITEM_REMOVE) or
                browser.find_elements(*CartLocators.MSG_EMPTY) or
                not browser.find_elements(*CartLocators.CART_BODY)
                )
            )
            btns = self.browser.find_elements(*CartLocators.BTN_ITEM_REMOVE)
            logger.info(f"clear_cart(self): Найдено разных товаров: {len(btns)} шт.")
            logger.debug(f"clear_cart(self): Найденные кнопки удаления товаров: {btns}")
                
            if not btns:
                msg = "clear_cart(self): Корзина была пуста и не нуждалась в очищении" if removed == 0 else "Корзина очищена"
                logger.info(msg)
                break
            
            btn = btns[0]
            try:
                ActionChains(self.browser).move_to_element(btn).perform()
                logger.debug("clear_cart(self): Навели мышку на кнопку удаления")

                btn.click()
                logger.debug("clear_cart(self): Кликнули по кнопке удаления")

                WebDriverWait(self.browser, 5).until(EC.staleness_of(btn))
                removed += 1
                logger.info(f"clear_cart(self): Товар №{removed} удалён из корзины")

            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                logger.warning(f"clear_cart(self): Не удалось удалить товар: {e}")
                repeat_counter += 1
                sleep(1)
                if repeat_counter >= max_stuck_repeats:
                    logger.error("clear_cart(self): Превышено число неудачных попыток — возможно, корзина застряла")
                    break

            except Exception as e:
                    logger.error(e)

        logger.info(f"clear_cart(self): Итог: из корзины было удалено {removed} товаров")  

    def is_empty(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(CartLocators.MSG_EMPTY)
            )
            empty_text = self.browser.find_element(*CartLocators.MSG_EMPTY)
            if empty_text:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f"is_empty(self): Ошибка при проверке пустоты корзины {e}")
            return False 

    def click_checkout_btn(self):
        logger.info("Пытаемся найти кнопку оформления заказа")
        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(CartLocators.BTN_CHECKOUT)
            )
            btn = self.browser.find_element(*CartLocators.BTN_CHECKOUT)
            btn.click()
            logger.info("Нажали кнопку оформления заказа")
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(CheckoutPageLocators.CHECKOUT_BODY)
            )
            logger.info("Перешли на страницу оформления заказа")
            return True

        except Exception as e:
            logger.error(f"Ошибка при оформлении заказа: {e}")
            return False
