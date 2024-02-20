from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "Акты"
def test_button_deeds(open_browser, auth_mz):
    button_deeds = BasePage(open_browser)
    button_deeds.button_main_menu().click()
    time.sleep(1)
    button_deeds.button_builders(3).click()
