import allure
import storage
from urllib.parse import urlparse
from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest

class TestRedirectDzen:

    @allure.title("Проверка редиректа на страницу Дзен после клика на логотип Яндекс")
    def test_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_homepage_and_close_cookie_window()
        main_page.click_to_lower_order_button()
        order_page.click_on_button_to_redirect_dzen()
        order_page.switch_to_next_window()

        actual_url = urlparse(order_page.current_url())
        expected_url = urlparse(storage.DZEN_URL)
        assert actual_url.scheme == expected_url.scheme
        assert actual_url.netloc == expected_url.netloc
        assert actual_url.path == expected_url.path