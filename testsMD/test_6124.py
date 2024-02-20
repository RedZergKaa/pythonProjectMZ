from pages.main_page import MainPage

# Фильтрация данных на панели индикаторов: Кварталам и годам отчётности
def test_filter_indicators(open_browser, auth_mz):
    method_object = MainPage(open_browser)
    method_object.filter_reports(67, MainPage.quart_selections)
    # Был сделан выбор по индексу, т.к. текст имеет римские цифры.