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
                               "//div/a[@class='toolbar__icons-item modal_tech_support']"]  # массив(лист) кнопок перехода из главного меню в
    # разделы АИС МЗ
    button_logout = "//div/a[@class='toolbar__icons-item exit']"  # локатор кнопки "Выйти"


# Функция массива по всем знакам вопроса на основной странице(локаторы)
def locate_tooltip():
    try:
        for i in range(1, 14):
            mas_tooltip = f"(//div[@class='question_sign'])[{i}]"   # массив локатора в котором xpath по знакам
            asyncio.sleep(1)    # асинхронный слип, для выполнения операции на фоне
            return mas_tooltip
    except IndexError:
        print('Ошибка элемента')

# Класс для определения переменных на главной странице
class MainPageEnvironment:
    report_button = "//select[@id='VPtopTenSelect']"    # Локатор кнопки выбора отчетов(фильтр)
    quart_selections = "//select[@id='current_quart']"  # Локатор выбора квартала/года на главной стр.
    # Локатор кнопки фильтра квартала/года
    button_filterYearAndQuarts = "(//span[@class='select2-selection__arrow'])[2]"
    search_field = "//input[@class='select2-search__field']"    # Локатор поля поиска в фильтре квартала/года
    # Локатор кнопки "Знак вопроса"
    button_sing_of_questions = "//button[@class='mdc-fab VPhelp']"