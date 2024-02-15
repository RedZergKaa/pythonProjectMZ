from pages.base_page import *
import time


# тест кнопки "Выйти" на страницу авторизации
def test_button_quit(open_browser, auth_mz):
    button_quit = Base_Page(open_browser)
    button_quit.logout().click()
    time.sleep(1)
