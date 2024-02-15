from pages.base_page import *
import time
#тест на переход из главного меню Портала АИС МЗ в раздел "Объекты"
def test_button_objects(open_browser, auth_mz):
    button_objects = Base_Page(open_browser)
    button_objects.button_main_menu().click()
    time.sleep(1)
    button_objects.button_builders(1).click()
    time.sleep(1)