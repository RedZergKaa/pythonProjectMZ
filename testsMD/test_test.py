from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Edge()
try:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.XPATH, "//body/div/form/div[6]/button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
