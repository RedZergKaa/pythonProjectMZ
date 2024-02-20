from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Нажатие на фильтр типа отчётов
def test_click_filter_report(open_browser, auth_mz):
    try:
        local_object = BasePage(open_browser)
        locator = "//*[@id='select2-VPtopTenSelect-container']"     # Локатор кнопки фильтра отчетов
        local_object.driver_wait_visibility(locator)
        open_browser.find_element(By.XPATH, locator).click()    # Клик по кнопке
    except Exception as e:
        print(e)