from selenium.common import NoSuchElementException
from config.variables_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Базовый класс для работы со страницей авторизации
class BasePage:
    def __init__(self, open_browser):
        self.fixture_one = open_browser  # конструктор для вызова фикстуры с драйвером браузера

    def open_link(self, url):
        try:
            self.fixture_one.get(url)
            link = WebDriverWait(self.fixture_one, 5).until(EC.visibility_of_element_located((By.ID,
                                                                                              "bx_breadcrumb_0")))
            return link  # функция для загрузки страницы
        except Exception as e:
            print(e)

    def login_field(self):
        try:
            return self.fixture_one.find_element(By.XPATH,
                                                 AuthTest.login_field)  # выполняет функцию поиска строки логина
        except Exception as e:
            print(e)  # закрывает драйвер браузера

    def pass_field(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.pass_field)  # выполняет функцию поиска строки пароля

    def login_button(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_click)  # выполняет функцию кнопки войти на странице
        # авторизации

    def button_main_menu(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_mainMENU)  # выполняет функцию поиска кнопки в главном
        # меню для перехода

    def button_builders(self, button):
        try:
            return self.fixture_one.find_element(By.XPATH, AuthTest.mas_buttons_in_mainMENU[button])  # функция
            # кнопок в массиве перехода в разделы

        except IndexError as e:
            print('Ошибка элемента', e)  #


    def logout(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_logout)  # выполняет функцию поиска кнопки в главном
        # меню для перехода
