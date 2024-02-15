from pages.base_page import *
import time


# тест на переход из главного меню Портала АИС МЗ в раздел "Аналитика"
def test_button_analytics(open_browser, auth_mz):
    button_analytics = Base_Page(open_browser)
    button_analytics.button_main_menu().click()
    time.sleep(1)
    button_analytics.button_builders(2).click()

    time.sleep(1)
