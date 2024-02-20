from pages.base_page import *

#тест на клик кнопки главное меню в АИС МЗ
def test_button_main_button(open_browser, auth_mz):
    test_button = BasePage(open_browser)
    test_button.button_main_menu().click()
