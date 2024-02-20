import os
import requests
import time
from pages.base_page import *
def test_download_file_about_system(open_browser, auth_mz):
    var = BasePage(open_browser)
    var.button_builders(8).click()
    # клик по кнопке "Cписок исправлений по версиям"
    open_browser.find_element(By.XPATH, "//a[contains(text(), 'Cписок исправлений по версиям')]").click()
    download_dir = "C:/Users/nebul/Downloads"   #директория куда скачается файл
    time.sleep(8)
    # Получение списка загруженных файлов из директории
    files = os.listdir(download_dir)
    # Логика: последний файл скачанный берется из списка в папке
    las_file = sorted(files, key=lambda x: os.path.getmtime(download_dir))[-1]
    # Открытие и обработка файла
    with open(os.path.join(download_dir, las_file), "rb") as file:
        file_con = file.read()  #проверка содержимого файла
        print(file_con)     # Вывод содержимого файла в консоль