import allure
import pytest
import storage
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize("index, answer",
                             [
            (0, storage.OTVET_1),
            (1, storage.OTVET_2),
            (2, storage.OTVET_3),
            (3, storage.OTVET_4),
            (4, storage.OTVET_5),
            (5, storage.OTVET_6),
            (6, storage.OTVET_7),
            (7, storage.OTVET_8)
        ]
                             )
    @allure.title("Тестирование блока Вопросы о важном ")
    def test_questions_block(self, driver, index, answer):
        main_page = MainPage(driver)
        main_page.open_homepage_and_close_cookie_window()
        assert main_page.get_answer_text(index) == answer