from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Edge()
    browser.get(link)

    input1 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    input1.click()

finally:
    time.sleep(15)
    browser.quit()
