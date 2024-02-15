from pages.base_page import *



# тест на переход из главного меню Портала АИС МЗ в раздел "Лог изменений"
def test_button_log(open_browser, auth_mz):
    button_log = BasePage(open_browser)
    button_log.button_main_menu().click()
    button_log.button_builders(5).click()
