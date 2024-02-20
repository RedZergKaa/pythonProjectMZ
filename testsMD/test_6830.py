from pages.base_page import *
from pages.main_page import MainPage
# Кнопка "Знак вопроса"
def test_sign_questions(open_browser, auth_mz):
    try:
        obj = MainPage(open_browser)
        # Функция кнопки "Знак вопроса"
        obj.button_sign_questions(MainPageEnvironment.button_sing_of_questions)
    except NoSuchElementException as e:
        print('Элемент не найден', e)