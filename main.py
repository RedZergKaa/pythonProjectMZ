from pages.base_page import *

class Test_MZ:

    def test_login(self, open_browser):
        BasePage(open_browser).open_link(link_to_MB)
