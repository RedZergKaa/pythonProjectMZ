from pages.main_page import *

# Тест: Подсказка знак вопроса на виджетах
def test_tooltips(open_browser, auth_mz):
    tooltip = MainPage(open_browser)
    tooltip.guidance_tooltip(locate_tooltip())

