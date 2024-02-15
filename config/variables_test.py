import asyncio

link_to_prodMB = "http://aismz.mosreg.ru/"  # ссылка на прод АИС МЗ
link_to_MB = "https://reliz.aismz.mosreg.ru/"  # ссылка на стейдж АИС МЗ
user_Name = "KrasavtsevAA"  # Логин пользователя АИС МЗ
user_Password = "12345678"  # Пароль пользователя АИС МЗ

#
class AuthTest:
    login_field = "//input[@id='inp_AUTH_LOGIN']"  # локатор переменной ввода логина
    pass_field = "//input[@id='inp_AUTH_PASSWORD']"  # локатор переменной ввода пароля
    button_click = "//input[@value='Войти']"  # локатор переменной кнопки войти
    button_mainMENU = "//div[@class='header__menuIcon']"  # локатор переменной кнопки в главном меню для перехода по
    # разделам
    mas_buttons_in_mainMENU = ["//div/a[@data-name='zastroyshchiki_menu']", "//div/a[@data-name='obekty_menu']",
                               "//div/a[@data-name='analytics_menu']", "//div/a[@data-name='deeds_menu']",
                               "//div/a[@data-name='nsi_menu']", "//div/a[@data-name='log_menu']",
                               "//div/a[@data-name='integer_menu']", "//div/a/span[text()='Техническая поддержка']",
                               "//div/a/span[text()='О системе']"]  # массив(лист) кнопок перехода из главного меню в
    # разделы АИС МЗ
    button_logout = "//div/a[@class='toolbar__icons-item exit']"  # локатор кнопки "Выйти"


def locate_tooltip():
    try:
        for i in range(1, 14):
            mas_tooltip = f"(//div[@class='question_sign'])[{i}]"   # массив локатора в котором xpath по знакам
            asyncio.sleep(1)
            return mas_tooltip
    except IndexError:
        print('Ошибка элемента')

class MainPageEnvironment:
    report_button = "//select[@id='VPtopTenSelect']"    # Локатор кнопки выбора отчетов(фильтр)