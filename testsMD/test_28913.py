from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "Справочники"
def test_button_nsi(open_browser, auth_mz):
    button_nsi = BasePage(open_browser)
    button_nsi.button_main_menu().click()
    time.sleep(1)
    button_nsi.button_builders(4).click()
