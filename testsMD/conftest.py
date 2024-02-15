from selenium import webdriver
import pytest
from pages.base_page import *


@pytest.fixture  #фикстура для запуска браузера
def open_browser():
    driver = webdriver.Edge()
    try:
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        print(e)
    finally:
        driver.quit()

@pytest.fixture  #фикстура для авторизации в АИС МЗ
def auth_mz(open_browser):
    base_page = BasePage(open_browser)  # Объект класса Base_Page
    base_page.open_link(link_to_MB)  # вызов функции для перехода по линку
    base_page.login_field().clear()  # Очистка поля логин, т.к. в поле при открытии прописывается Undefined
    base_page.login_field().send_keys(user_Name)  # Попытка ввода в поле логин
    assert base_page.login_field().get_attribute('id') == "inp_AUTH_LOGIN"
    base_page.pass_field().send_keys(user_Password)  # Попытка ввода в поле пароля
    base_page.login_button().click()  # Функция клика по кнопке "ВХОД"
