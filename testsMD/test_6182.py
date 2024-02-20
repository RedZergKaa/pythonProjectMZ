from pages.base_page import *
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC

# Поиск в фильтрации данных на панели индикаторов: Кварталам и годам отчётности
def test_search_filter(open_browser, auth_mz):
    try:
        # Клик по кнопке фильтра квартала/года
        open_browser.find_element(By.XPATH, MainPage.button_filterYearAndQuarts).click()
        # В поле поиск введение искомого значения
        open_browser.find_element(By.XPATH, MainPage.search_field).send_keys("2021")
        # Запись локатора найденных результатов
        results_list = open_browser.find_element(By.XPATH, "//ul[@class='select2-results__options']")
        # Проверка условия найденного результата и что поиск прошел как нужно
        if results_list.get_attribute("id") == "select2-current_quart-results":
            # Клик по найденному элементу(в тесте 2021 год)
            results_list.find_element(By.XPATH, ".//*[text()='I / 2021']").click()
            # Локатор для ожидания, т.к. обновление после выбора года длинное
            var = open_browser.find_element(By.XPATH, "//span[@id='select2-current_quart-container']")
            WebDriverWait(open_browser, 15).until(EC.visibility_of(var))  # Ожидание, пока элемент станет видимым
        else:
            print("Определения по ID-квартала нет")
    except Exception as e:
        print(e)