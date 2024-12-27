from datetime import datetime
import allure
import storage

from locators.locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    @staticmethod
    def get_locator_by_color(color):
        if color == 'black':
            return OrderPageLocators.COLOR_BLACK
        elif color == 'grey':
            return OrderPageLocators.COLOR_GREY
        else:
            raise ValueError(f"Неверный цвет: {color}. Допустимые значения: 'black' или 'grey'")

    def select_current_day(self):

        current_date = datetime.now()
        self.click_to_element(OrderPageLocators.DATE_DELIVERY_SAMOKAT)

        current_day = current_date.day
        locator_current_day = self.format_locators(OrderPageLocators.CALENDAR_CLICK, current_day)
        self.click_to_element(locator_current_day)

    @staticmethod
    def remove_new_lines_and_spaces(text):
        return "".join(text.split())

    @allure.step("Создание заказа с указанными параметрами")
    def set_order(self, name, surname, address, phone, metro_station, color_scooter, days_rental, comment_for_courier):

        self.add_text_to_element(OrderPageLocators.NAME_FIELD, name)
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, address)

        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.add_text_to_element(OrderPageLocators.METRO_FIELD,
                                 'а')  # Добавляю символ а, чтобы список открылся

        select_station = self.format_locators(OrderPageLocators.METRO_LIST, metro_station)
        element = self.find_element_with_wait(select_station)
        self.wait.until(EC.visibility_of(element))
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, phone)

        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

        self.find_element_with_wait(OrderPageLocators.DATE_DELIVERY_SAMOKAT)

        self.select_current_day()

        element_rental_field = self.find_element_with_wait(OrderPageLocators.TIME_RENTAL_FIELD)
        self.wait.until(EC.element_to_be_clickable(element_rental_field))
        element_rental_field.click()
        rental_period = self.format_locators(OrderPageLocators.TIME_RENTAL, days_rental)
        element_rental = self.find_element_with_wait(rental_period)
        self.wait.until(EC.visibility_of(element_rental))
        self.wait.until(EC.element_to_be_clickable(element_rental))
        element_rental.click()

        color_test = OrderPage.get_locator_by_color(color_scooter)
        self.click_to_element(color_test)

        self.add_text_to_element(OrderPageLocators.COMMENT, comment_for_courier)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_FROM_FORM)
        self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Проверка статуса заказа")
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ACCEPT_ORDER)

    @allure.step("Переход на вкладу Дзен")
    def switch_to_next_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_dzen_url(storage.DZEN_URL, 15)

    @allure.step("Проверяется статус заказа и дальнейшее закрытие окна")
    def check_status_and_close_window(self):
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.STATUS_BUTTON))
        self.click_to_element(OrderPageLocators.STATUS_BUTTON)
        self.find_element_with_wait(OrderPageLocators.BUTTON_FOR_REDIRECT_DZEN)

    @allure.step("Нажимаем на логотип Яндекс чтобы открылся Дзен")
    def click_on_button_to_redirect_dzen(self):
        self.click_to_element(OrderPageLocators.DZEN_LOGO_URL)