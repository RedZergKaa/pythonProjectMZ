from pages.base_page import *
import time
#тест на переход страницы прода Мониторинг застройщика
def test_link_prod(open_browser):
    open_browser.get(link_to_prodMB)
    time.sleep(2)
