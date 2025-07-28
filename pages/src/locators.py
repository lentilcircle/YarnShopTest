from selenium.webdriver.common.by import By

class BasePageLocators:
    TOP_HEADER = (By.CSS_SELECTOR, ".header__top")
    
    BOTTOM_HEADER = (By.CSS_SELECTOR, ".header__bottom")
    BH_LOGO = (By.CSS_SELECTOR, "")
    BH_TITLE = (By.CSS_SELECTOR, "")
    BH_BTN_PRYAZA_CATALOG = (By.CSS_SELECTOR, ".header-nav__item:first-child .header-nav__link")
    BH_BTN_TKAN_CATALOG = (By.CSS_SELECTOR, "")
    BH_BTN_FURNITURA_CATALOG = (By.CSS_SELECTOR, "")
    BH_BTN_LITERATURA_CATALOG = (By.CSS_SELECTOR, "")
    BH_BTN_SALE_CATALOG = (By.CSS_SELECTOR, "")
    BH_BTN_SEARCH = (By.CSS_SELECTOR, ".search-trigger")
    SEARCH_POPUP_ACTIVE = (By.CSS_SELECTOR, ".search-popup.js-active")
    SEARCH_BTN_CLOSE = (By.CSS_SELECTOR, ".search_close")
    BH_BTN_CART = (By.CSS_SELECTOR, "#header-cart")

    TOP_FOOTER = (By.CSS_SELECTOR, "")

    BOTTOM_FOOTER = (By.CSS_SELECTOR, "")

    LINKS_FOOTER = (By.CSS_SELECTOR, "")

class MainPageLocators(BasePageLocators):
    NEWS_SLIDER = (By.CSS_SELECTOR, "")
    
    NEW_ITEMS_BLOCK = (By.CSS_SELECTOR, "#new_products_container")

    PROMO_BLOCK = (By.CSS_SELECTOR, "")
    
    SEO_BLOCK = (By.CSS_SELECTOR, "")
    
class CatalogPageLocators(BasePageLocators): pass

class ItemCardLocators(BasePageLocators):
    ITEM_CARD_PIC = (By.CSS_SELECTOR, ".item-image")
    ITEM_CARD_NAME = (By.CSS_SELECTOR, ".item-name")
    ITEM_NAME_LINK = (By.CSS_SELECTOR, ".item-name a")
    ITEM_CARD_PRICE = (By.CSS_SELECTOR, ".item-price")

class ItemPageLocators(BasePageLocators):
    PRODUCT_WRAP = (By.CSS_SELECTOR, ".product__wrap")
    ITEM_PIC = (By.CSS_SELECTOR, ".product__image__big")
    ITEM_NAME = (By.CSS_SELECTOR, ".product__content .product__title")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product__content .product__price")
    BTN_ADD = (By.CSS_SELECTOR, ".product__add.btn-shadow")
    BTN_ADDED = (By.CSS_SELECTOR, ".product__add.btn-shadow.added")

class CartLocators:
    CART_BODY = (By.CSS_SELECTOR, "#modal-basket")
    ITEM_PICS_IN_CART = (By.CSS_SELECTOR, "#modal-basket .item-image")
    ITEM_NAMES_IN_CART = (By.CSS_SELECTOR, "#modal-basket .item-name")
    ITEM_PRICES_IN_CART = (By.CSS_SELECTOR, "#modal-basket .item-price")
    ITEM_COSTS = (By.CSS_SELECTOR, ".summ_val")
    TOTAL_WITHOUT_DISCOUNT = (By.CSS_SELECTOR, ".total_without_discont")
    BTN_ITEM_REMOVE = (By.CSS_SELECTOR, ".item-remove")
    BTN_CLOSE = (By.CSS_SELECTOR, "#modal-basket .fancybox-close-small")
    BTN_CHECKOUT = (By.CSS_SELECTOR, ".check-out")
    MSG_EMPTY = (By.CSS_SELECTOR, ".modal-basket-empty")

class CheckoutPageLocators:
    CHECKOUT_BODY = (By.CSS_SELECTOR, "#order_form_content")