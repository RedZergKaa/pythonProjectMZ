from pages.base_page import *



# тест на проверку открытия и перехода по линку в Мониторинг Застройщика
def test_enter_mz(open_browser):
    open_browser.get(link_to_MB)

