from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "О системе"
def test_button_aboutsystem(open_browser, auth_mz):
    button_aboutsystem = BasePage(open_browser)
    button_aboutsystem.button_main_menu().click()
    time.sleep(1)
    button_aboutsystem.button_builders(7).click()
    time.sleep(1)
