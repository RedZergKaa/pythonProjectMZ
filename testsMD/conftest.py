from selenium import webdriver
import pytest
from pages.base_page import *


@pytest.fixture  #фикстура для запуска браузера
def open_browser():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture #фикстура для авторизации в АИС МЗ
def auth_mz(open_browser):
    base_page = Base_Page(open_browser)  # Объект класса Base_Page
    base_page.open_link(link_to_MB)  # вызов функции для перехода по линку
    base_page.login_field().clear()  # Очистка поля логин, т.к. в поле при открытии прописывается Undefind
    base_page.login_field().send_keys(user_Name)  # Попытка ввода в поле логин
    assert base_page.login_field().get_attribute('id') == "inp_AUTH_LOGIN"
    base_page.pass_field().send_keys(user_Password)  # Попытка ввода в поле пароля
    base_page.login_button().click()  # Функция клика по кнопке "ВХОД"
