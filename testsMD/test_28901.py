from pages.base_page import *
import time
#тест на переход из главного меню Портала АИС МЗ в раздел "Застройщики"
def test_button_zastroyaschiki(open_browser, auth_mz):
    button_zasstroyaschiki = Base_Page(open_browser)
    button_zasstroyaschiki.button_main_menu().click()
    time.sleep(1)
    button_zasstroyaschiki.button_builders(0).click()
    time.sleep(1)
