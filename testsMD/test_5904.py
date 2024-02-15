from pages.main_page import MainPage


# Фильтрация данных на панели индикаторов: Необработанные отчёты
def test_filter_report(open_browser, auth_mz):
    filter_reports = MainPage(open_browser)
    filter_reports.filter_reports(1)
