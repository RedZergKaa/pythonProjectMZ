from pages.base_page import *
import re

# Описание модального окна "О системе"
def test_overwiew_system(open_browser, auth_mz):
    method_object = BasePage(open_browser)
    method_object.button_builders(8).click()
    # Локаторы данных полей для проверки в разделе "О системе"
    version_element = open_browser.find_element(By.XPATH, "//div[contains(text(), 'Версия:')]")
    release_date_element = open_browser.find_element(By.XPATH, "//div[contains(text(), 'Дата релиза:')]")
    user_element = open_browser.find_element(By.XPATH, "//div[contains(text(), 'Пользователь:')]")
    email_element = open_browser.find_element(By.XPATH, "//div[contains(text(), 'Email:')]")
    # Компиляция локаторов в регулярные выражения, для динамики версий и даты
    version_pattern = re.compile(r"Версия: \d+\.\d+\.\d+\.\d+")
    release_date_pattern = re.compile(r"Дата релиза: \d{2}\.\d{2}\.\d{4}")
    # Проверки отображения корректных данных в полях
    assert version_pattern.match(version_element.text)
    assert release_date_pattern.match(release_date_element.text)
    assert user_element.text == "Пользователь: Андрей Красавцев Александрович"
    assert email_element.text == "Email: KrasavtsevAA@mosreg.ru"
    # Локатор самого окна раздела "О системе"
    locator_system_window = "//div[contains(text(), 'О системе')]"
    # Ожидание окна
    method_object.driver_wait_visibility(locator_system_window)
    # СОхранение скриншота с данными
    capture_screenshot = 'E:/WinRepire/CaptureScreenshot.png'
    open_browser.save_screenshot(capture_screenshot)

