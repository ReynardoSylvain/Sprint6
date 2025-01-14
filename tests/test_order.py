import allure
import storage
from urllib.parse import urlparse
from helper import generate_phone_number
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Тест заказа самоката")
    @allure.description("Создание заказа кликом на верхнюю кнопку Заказать")
    def test_order_and_redirect_to_homepage(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_homepage_and_close_cookie_window()
        main_page.click_to_upper_order_button()
        order_page.set_order(storage.NAME,
                             storage.SURNAME,
                             storage.ADDRESS,
                             generate_phone_number(),
                             storage.METRO_STATION,
                             storage.COLOR,
                             storage.DAYS,
                             storage.COMMENT)
        assert 'Заказ оформлен' in order_page.check_order()
        order_page.check_status_and_close_window()

    @allure.title("Тест заказа самоката")
    @allure.description("Создание заказа кликом на нижнюю кнопку Заказать")
    def test_order_and_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.open_homepage_and_close_cookie_window()
        main_page.click_to_lower_order_button()
        order_page.set_order(storage.NAME_2,
                             storage.SURNAME_2,
                             storage.ADDRESS_2,
                             generate_phone_number(),
                             storage.METRO_STATION_2,
                             storage.COLOR_2,
                             storage.DAYS_2,
                             storage.COMMENT_2)
        assert 'Заказ оформлен' in order_page.check_order()