from selenium.common import NoSuchElementException
from selenium.webdriver.edge.options import Options
from config.variables_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# Базовый класс для работы со страницей авторизации
class Base_Page:
    def __init__(self, open_browser):
        self.fixture_one = open_browser  # конструктор для вызова фикстуры с драйвером бразуера

    def open_link(self, url):
        try:
            self.fixture_one.get(url)
            link = WebDriverWait(self.fixture_one, 5).until(EC.visibility_of_element_located((By.ID,
                                                                                              "bx_breadcrumb_0")))
            return link  # функция для загрузки страницы
        except NoSuchElementException:
            print('Элемент не найден')

    def login_field(self):
        try:
            return self.fixture_one.find_element(By.XPATH,
                                                 AuthTest.login_field)  # выполняет функцию поиска строки логина
        except NoSuchElementException:
            print('Элемент не найден')  # закрывает драйвер бразуера

    def pass_field(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.pass_field)  # выполняет функцию поиска строки пароля

    def login_button(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_click)  # выполняет функцию кнопки войти на странице авторизации

    def button_main_menu(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_mainMENU)  # выполняет функцию поиска кнопки в главном меню для перехода

    def button_builders(self, button):
        try:
            return self.fixture_one.find_element(By.XPATH, AuthTest.mas_buttons_in_mainMENU[button])  # функция кнопок в массиве перехода в разделы

        except LookupError:
            print('Ошибка элемента')  #


    def logout(self):
        return self.fixture_one.find_element(By.XPATH,
                                             AuthTest.button_logout)  # выполняет функцию поиска кнопки в главном меню для перехода



