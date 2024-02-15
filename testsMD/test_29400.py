from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Нажатие на фильтр типа отчётов
def test_click_filter_report(open_browser, auth_mz):
    open_browser = WebDriverWait(open_browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*["
                                                                                                     "@id='select2"
                                                                                                     "-VPtopTenSelect"
                                                                                                     "-container']")))
    open_browser.find_element(By.XPATH, "//*[@id='select2-VPtopTenSelect-container']").click()
