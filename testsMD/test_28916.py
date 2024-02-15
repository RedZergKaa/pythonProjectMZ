from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "Техническая поддержка"
def test_button_techsupp(open_browser, auth_mz):
    button_techsupp = Base_Page(open_browser)
    button_techsupp.button_main_menu().click()
    time.sleep(1)
    button_techsupp.button_builders(8).click()
    time.sleep(1)
