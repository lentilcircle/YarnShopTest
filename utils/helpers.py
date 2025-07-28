from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def normalize(text):
    return text.lower().strip()

def normalize_price(price: str):
    return int(''.join(filter(str.isdigit, price)))

def wait_until_cart_ready(): pass

def wait_until_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_until_clickable(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )