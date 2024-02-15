from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#тест на переход из главного меню Портала АИС МЗ в раздел ""

def test_filter_report(open_browser, auth_mz):

    select = Select(open_browser.find_element(By.XPATH, "//select[@id='VPtopTenSelect']"))
    select.select_by_index(2)
    time.sleep(4)






