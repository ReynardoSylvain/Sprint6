from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.wait.until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_dzen_url(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))

    def current_url(self):
        return self.driver.current_url

    @staticmethod
    def format_locators(locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator