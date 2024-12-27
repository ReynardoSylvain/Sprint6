import allure
import storage
from pages.main_page import MainPage


class TestRedirectHomepage:

    @allure.title("Проверка перехода на главную страницу после клика на логотип Самокат")
    def test_redirect_to_homepage(self, driver):
        main_page = MainPage(driver)
        main_page.open_homepage_and_close_cookie_window()
        main_page.click_to_logo_samokat()
        assert main_page.current_url() == storage.HOMEPAGE_URL