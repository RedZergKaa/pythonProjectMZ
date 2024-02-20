from pages.base_page import *

# Переход в поддержку
def test_link_to_supp(open_browser, auth_mz):
    method_object = BasePage(open_browser)
    method_object.button_builders(8).click() # Открытие "О системе"
    # локатор ссылки переходжа на техсап
    open_browser.find_element(By.XPATH, "//a[contains(text(), "
                                        "'http://reliz.aismz.mosreg.ru/tech-support/')]").click()
    # Локатор для проверки, открытия раздела техсапа
    tech_supp_locator = open_browser.find_element(By.XPATH, "(//span[contains(text(),'Техническая поддержка')])[2]")
    # Проверка открытия техсапа
    assert tech_supp_locator.text == "Техническая поддержка"