from selenium.common import NoSuchElementException
from selenium.webdriver.edge.options import Options
from config.variables_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


# Базовый класс работы со стартовой страницей АИС МЗ
class MainPage(BasePage, MainPageEnvironment):

    # Функция обработки наведения мышки на знаки вопроса на виджетах
    def guidance_tooltip(self, locator):
        try:
            element = self.fixture_one.find_element(By.XPATH, locator)  # Локатор виджета
            hover = ActionChains(self.fixture_one).move_to_element(element)     # Наведение на элемент
            hover.perform()
            tooltip = WebDriverWait(self.fixture_one, 6).until(
                EC.visibility_of_element_located((By.XPATH, locator)))  # ожидание появления подсказки
            return tooltip
        except NoSuchElementException:
            print('Элемент не найден')

    # Функция селектор для выбора на главной странице фильтра отчетности(с нарушениями и без)
    def filter_reports(self, index, report):
        try:
            BasePage.driver_wait_visibility(self, report)  # Ожидание
            select = Select(self.fixture_one.find_element(By.XPATH, report))    # Переменная локатора
            select.select_by_index(index)
        except IndexError:
            print('Ошибка элемента')  # Метод фильтра отчётов

    # Функция кнопки "Знак вопроса"
    def button_sign_questions(self, locator):
        try:
            self.fixture_one.find_element(By.XPATH, locator)
            BasePage.driver_wait_visibility(self, locator)
        except NoSuchElementException as e:
            print('Элемент не найден', e)