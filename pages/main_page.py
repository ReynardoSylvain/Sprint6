import allure
import storage
from locators.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step("Открываем главную страницу и принимаем куки")
    def open_homepage_and_close_cookie_window(self):
        self.open_page(storage.HOMEPAGE_URL)
        self.click_to_element(MainPageLocators.COOKIES_BUTTON)

    @allure.step("Смотрим текст ответа под вопросами в главен Вопросы о важном")
    def get_answer_text(self, index):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_BUTTONS, index)
        locator_a_formatted = self.format_locators(MainPageLocators.QUESTION_TEXT, index)
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.QUESTION_SECTION))
        self.scroll_to_element(locator_q_formatted)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)



    @allure.step("Возврат на главную страницу по клику на логотип Самокат")
    def click_to_logo_samokat(self):
        self.click_to_element(MainPageLocators.SAMOKAT_LOGO)

    @allure.step("Нажимаем на кнопку Заказать в правом верхнем углу страницы")
    def click_to_upper_order_button(self):
        self.click_to_element(MainPageLocators.UP_ORDER_BUTTON)

    @allure.step("Нажимаем на кнопку Заказать в центре внизу страницы")
    def click_to_lower_order_button(self):
        self.click_to_element(MainPageLocators.LOW_ORDER_BUTTON)