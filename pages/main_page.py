from selenium.common import NoSuchElementException
from selenium.webdriver.edge.options import Options
from config.variables_test import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Base_Page
from selenium.webdriver.support.ui import Select


# Базовый класс для работы со
class MainPage(Base_Page):

    def guidance_tooltip(self, locator):
        element = self.fixture_one.find_element(By.XPATH, locator)
        hover = ActionChains(self.fixture_one).move_to_element(element)
        hover.perform()
        tooltip = WebDriverWait(self.fixture_one, 6).until(
            EC.visibility_of_element_located((By.XPATH, locator)))
        return tooltip                  #

    def filter_reports(self, index):
        try:
            report = MainPageEnvironment.report_button
            select = Select(self.fixture_one.find_element(By.XPATH, report))
            select.select_by_index(index)
        except IndexError:
            print('Ошибка элемента')  #