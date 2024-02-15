from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "Интеграция"
def test_button_integer(open_browser, auth_mz):
    button_integer = BasePage(open_browser)
    button_integer.button_main_menu().click()
    time.sleep(1)
    button_integer.button_builders(6).click()
    time.sleep(1)
