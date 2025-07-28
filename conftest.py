import pytest
import allure
from seleniumwire import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.MainPage import MainPage
from pages.CartPage import CartModal
from utils.logger import logger
from utils.paths import SUPPORTED_BROWSERS


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default = "chrome",
        help="Выбор браузера для тестов." \
        f"Поддерживаемые браузеры: {SUPPORTED_BROWSERS}" \
        "По умолчанию: chrome."
        "(Пример: --browser=edge)"
    )



@pytest.fixture(scope="class")
@allure.step("Создать браузер для теста")
def browser(request):
   
    browser_name = request.config.getoption("--browser").lower()

    if browser_name not in SUPPORTED_BROWSERS:
        raise pytest.UsageError(f"Браузер '{browser_name}' не поддерживается."
                                f"Поддерживаются: {SUPPORTED_BROWSERS}")

    logger.info(f"setup: Запуск тестов в браузере: {browser_name}")

    browser = None

    try:
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument("--log-level=3")
            options.page_load_strategy = 'eager'
            browser = webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.page_load_strategy = 'eager'
            browser = webdriver.Firefox(options=options)

        elif browser_name == "edge":
            options = EdgeOptions()
            options.page_load_strategy = 'eager'
            browser = webdriver.Edge(options=options)

        def fin():
            try:
                logger.info("teardown: Start")
                page = MainPage(browser)
                cart = CartModal(browser)

                page.open_cart()

                if not cart.is_empty():
                    logger.info(f"teardown: Требуется очистка корзины. Начинаем очистку корзины")
                    try:
                        cart.clear_cart()
                    except Exception as e:
                        logger.error(f"teardown: Не удалось закончить очистку корзину: {e}")
                else:
                    logger.info(f"teardown: Очистка корзины не требуется")

            except Exception as e:
                    logger.error(f"teardown: {e}")
                    
            finally:
                if browser:
                    logger.info("teardown: Закрытие браузера через driver.quit()")
                    browser.quit()

        request.addfinalizer(fin)
        browser.set_window_size(1280, 720)
        return browser

    except WebDriverException as e:
        logger.warning(f"setup: {browser_name} не запущен — пропуск теста: {e}")
        pytest.skip(f"setup: {browser_name} не запущен — пропуск теста: {e}")
        return None

    except Exception as e:
        logger.error(f"setup: Ошибка при запуске браузера {browser_name}: {e}")
        raise