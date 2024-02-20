from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import *
import time
import re
#тест на переход из главного меню Портала АИС МЗ в раздел ""

def test_filter_report(open_browser, auth_mz):
    method_object = BasePage(open_browser)
    method_object.button_builders(8).click()

