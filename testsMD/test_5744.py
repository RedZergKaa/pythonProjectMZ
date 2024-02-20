from pages.base_page import *
import time
# тест на авторизацию в Мониторинг Застройщика
def test_auth_mz(open_browser):
    base_page = BasePage(open_browser)  #Объект класса Base_Page
    base_page.open_link(link_to_MB)     #вызов функции для перехода по линку
    base_page.login_field().clear()     #Очистка поля логин, т.к. в поле при открытии прописывается Undefined
    base_page.login_field().send_keys(user_Name)    #Попытка ввода в поле логин
    time.sleep(2)   #Две секунды ожидания
    base_page.pass_field().send_keys(user_Password)     #Попытка ввода в поле пароля
    base_page.login_button().click()    #Функция клика по кнопке "ВХОД"
    time.sleep(2)
