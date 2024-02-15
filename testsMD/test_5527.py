from pages.base_page import *
import time
# тест на проверку ввода валидного логина в поле логина
def test_login(open_browser):
    base_page = Base_Page(open_browser)  # Объект класса Base_Page
    base_page.open_link(link_to_MB)  # вызов функции для перехода по линку
    base_page.login_field().clear()  # Очистка поля логин, т.к. в поле при открытии прописывается Undefind
    base_page.login_field().send_keys(user_Name)  # Попытка ввода в поле логин
    assert base_page.login_field().get_attribute('id') == "inp_AUTH_LOGIN"
    time.sleep(2)  # Две секунды ожидания
