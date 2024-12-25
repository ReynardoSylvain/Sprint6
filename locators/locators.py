from selenium.webdriver.common.by import By

# Локаторы на главной странице
class MainPageLocators:

    QUESTION_BUTTONS = By.ID, "accordion__heading-{}"
    QUESTION_TEXT = By.ID, "accordion__panel-{}"
    QUESTION_SECTION = By.ID, "accordion__heading-7"
    COOKIES_BUTTON = By.XPATH, "//button[@id='rcc-confirm-button']"
    UP_ORDER_BUTTON = By.XPATH, "(//button[@class='Button_Button__ra12g'])[1]"
    LOW_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton__')]//button"
    SAMOKAT_LOGO = By.XPATH, "//img[@alt='Scooter']"

# Локаторы на странице заказа
class OrderPageLocators:

    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_LIST = By.XPATH, "//ul[contains(@class, 'select-search')]//li[@data-index='{}']"
    PHONE_NUMBER_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    DZEN_LOGO_URL = By.XPATH, "//a[starts-with(@class, 'Header_LogoYandex')]" # Переход на страницу яндекс дзен
    BUTTON_NEXT = By.XPATH, "//button[contains(text(),'Далее')]"
    DATE_DELIVERY_SAMOKAT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR_FIELD = By.XPATH, "//div[contains(@class, 'react-datepicker__month-container')]"
    CALENDAR_CLICK = By.XPATH, "//div[contains(@class, 'react-datepicker__month')]//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month')) and text()='{}']"
    TIME_RENTAL = By.CSS_SELECTOR, "div[class='Dropdown-menu'] div:nth-child({})"
    TIME_RENTAL_FIELD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    COLOR_BLACK = By.XPATH, "//input[@id='black']"
    COLOR_GREY = By.XPATH, "//input[@id='grey']"
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    STATUS_BUTTON = By.XPATH, "//button[contains(text(),'Посмотреть статус')]"
    BUTTON_FOR_REDIRECT_DZEN = By.XPATH, "//img[@alt='Yandex']"
    BUTTON_YES = By.XPATH, "//button[contains(text(),'Да')]"
    ACCEPT_ORDER = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
    ORDER_BUTTON_FROM_FORM = By.XPATH, "(//button[@class='Button_Button__ra12g Button_Middle__1CSJM'])[1]"
