from pages.base_page import *
import time
# тест на проверку ввода валидного пароля в поле пароля
class Test_pass_field:

    def test_pass_field(self, open_browser):

        base_page = Base_Page(open_browser)
        base_page.open_link(link_to_MB)
        base_page.pass_field().send_keys(user_Password)
        time.sleep(2)