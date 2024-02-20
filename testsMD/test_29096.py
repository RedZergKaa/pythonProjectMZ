from pages.base_page import *


# тест кнопки "Выйти" на страницу авторизации
def test_button_quit(open_browser, auth_mz):
    button_quit = BasePage(open_browser)
    button_quit.logout().click()
