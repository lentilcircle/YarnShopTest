import pytest
import allure
from pages.MainPage import MainPage
from pages.CatalogPage import CatalogPage
from pages.ItemPage import ItemPage
from pages.CartPage import CartModal
from pages.src.urls import Pages
from pages.src.locators import (
    ItemPageLocators, ItemCardLocators, CartLocators)
from utils.helpers import normalize, normalize_price


class TestSmoke:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.catalog_page = CatalogPage(browser)
        self.item_page = ItemPage(browser)
        self.cart_page = CartModal(browser)

    @pytest.mark.parametrize("url", [Pages.MAIN_PAGE])
    @allure.title("Главная страница открывается")
    def test_main_page_should_open(self, url):
        
        with allure.step("Открыть главную страницу"):
            self.main_page.open_page(url)
            curr_url = self.main_page.get_current_url()
            assert "ili-ili" in curr_url, \
                f"Ошибка в url страницы. Текущий url: {curr_url}"

        with allure.step("Получить код состояния"):
            status_code = self.main_page.get_status_code()
            assert status_code == 200, \
                f"Сервер не ответил 200. Полученный ответ: {status_code}"

        with allure.step("Проверить, что страница не пуста"):
            assert self.main_page.is_not_empty, "Открытая страница пуста"

    @allure.title("Каталог открывается")
    def test_catalog_should_open(self):

        with allure.step("Открыть каталог пряжи"):
            url = self.main_page.open_catalog()
            assert "/catalog/" in url, \
                f"Ошибка в url страницы. Текущий url: {url}"

        with allure.step("Получить код состояния"):
            status_code = self.main_page.get_status_code()
            assert status_code == 200, \
                f"Сервер не ответил 200. Полученный ответ: {status_code}"

        with allure.step("Проверить, что страница не пуста"):
            assert self.main_page.is_not_empty, "Страница пуста"

    @pytest.mark.parametrize("element, description",
                             [(ItemCardLocators.ITEM_CARD_PIC, "Изображение товара"),
                              (ItemCardLocators.ITEM_CARD_NAME, "Название товара"),
                              (ItemCardLocators.ITEM_CARD_PRICE, "Цена товара")])
    @allure.title("Карточка товара: отображение основной информации")
    @allure.description("Проверка видимости изображения, названия и цены на карточке товара")
    def test_item_card_check_main_elements(self, element, description):
        with allure.step(f"Проверить видимость элемента карточки товара: {description}"):
            is_visible = self.catalog_page.check_element(element)
            assert is_visible, \
                f"Элемент {description} не был найден на карточке товара"

    @allure.title("Карточка товара ведет на страницу товара")
    def test_item_card_should_lead_to_item_page(self):
        with allure.step("Открыть страницу первого в списке товара кликом по картинке товара"):
            assert self.catalog_page.open_first_item_page(), \
                "Клик по картинке товара не привел на страницу товара"

    @pytest.mark.parametrize("element, description",
                            [(ItemPageLocators.ITEM_PIC, "Изображение товара"),
                            (ItemPageLocators.ITEM_NAME, "Название товара"),
                            (ItemPageLocators.ITEM_PRICE, "Цена товара"),
                            (ItemPageLocators.BTN_ADD, "Кнопка добавления в корзину")])
    @allure.title("Страница товара: отображение основных элементов")
    def test_item_page_check_main_elements(self, element, description):
        with allure.step(f"Проверить видимость элемента '{description}'"):
            is_visible = self.item_page.check_element(element)
            assert is_visible, \
                f"Элемент '{description}' не был найден на странице товара"

    @allure.title("Страница товара: добавление товара в корзину")
    def test_item_page_adding_item_to_cart(self):
        with allure.step("Добавить товар в корзину"):
            assert self.item_page.add_item_to_cart(), \
                "Товар не был добавлен в корзину"
    
    @allure.title("Корзина открывается")
    def test_cart_should_open(self):
        with allure.step("Открыть корзину"):
            assert self.item_page.open_cart(), "Корзина не открылась"

    @pytest.mark.parametrize("element, description",
                            [(CartLocators.ITEM_PICS_IN_CART, "Изображение товара"),
                            (CartLocators.ITEM_NAMES_IN_CART, "Название товара"),
                            (CartLocators.ITEM_PRICES_IN_CART, "Цена товара"),
                            (CartLocators.BTN_CHECKOUT, "Кнопка оформления заказа")])
    @allure.title("Корзина: отображение основных элементов")
    def test_cart_check_main_elements(self, element, description):
        with allure.step(f"Проверить видимость элемента корзины: {description}"):
            is_visible = self.cart_page.check_element(element)
            assert is_visible, \
                f"Элемент {description} не был найден в корзине"

    @allure.title("Корзина: кнопка оформления заказа ведет на страницу оформления")
    def test_checkout_btn_lead_to_chekout_page(self):
        with allure.step("Оформить заказ кликом по кнопке оформления заказа"):
            assert self.cart_page.click_checkout_btn(), "Заказ не был оформлен"

    #@pytest.mark.parametrize("element",
    #                        [ItemCardLocators.ITEM_CARD_PIC,
    #                        ItemCardLocators.ITEM_CARD_NAME,
    #                        ItemCardLocators.ITEM_CARD_PRICE])
    #@allure.title("Страница оформления заказа: отображение основных блоков")
    #def checkout_page_check_main_elements(self): pass




