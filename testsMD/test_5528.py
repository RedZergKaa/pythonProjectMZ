from pages.base_page import *
import time
# тест на проверку ввода валидного пароля в поле пароля
def test_pass_field(open_browser):

        base_page = BasePage(open_browser)
        base_page.open_link(link_to_MB)
        base_page.pass_field().send_keys(user_Password)
        time.sleep(2)