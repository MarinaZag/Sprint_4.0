import allure
import pytest
from pages.main_page import MainPage
from conftest import driver
from data.data import AnswerData

@allure.feature('Действия на главной странице с блоком вопросов')
class TestQuestionsSections:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Раздел «Вопросы о важном» - при клике на вопрос открывается соответствующий ответ')
    @pytest.mark.parametrize("num,text", AnswerData.sections_test_data)
    def test_get_answer(self, driver, num, text):
        main_page = MainPage(driver)
        main_page.main_url()
        main_page.scroll_question_path()
        main_page.click_on_question(num)
        current_answer = main_page.get_answers()
        assert current_answer == text
