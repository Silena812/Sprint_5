from selenium.webdriver.common.by import By


class Locators:

    ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a/p") # Кнопка Личный Кабинет
    REG_LINK = [By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a"] # ссылка Зарегистрироваться
    USER_NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input") # Имя в форме регистрации
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Имэйл в форме регистрации
    PASSWORD = (By.XPATH, "//input[@name= 'Пароль']") # Пароль в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка Зарегистрироваться в форме регистрации
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p") # Сообщение "Некорректный пароль"

    ENTER_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")  # Кнопка Войти в аккаунт на главной странице
    ENTER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button") # Кнопка Войти в форме логина
    MAKE_ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") # Кнопка Оформить заказ
    ENTER_LINK = (By.XPATH, "// *[ @ id = 'root'] / div / main / div / div / p / a") # ссылка Войти в форме регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a") # ссылка Восстановить пароль

    CONSTRUCTOR = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") # Кнопка Конструктор
    LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div") # Логотип

    EXIT_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button") # Кнопка Выйти в личном кабинете

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div") # таб Булки
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div") # таб Соусы
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div") # таб Начинки

    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']") # раздел Булки
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']")  # раздел Соусы
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']") # раздел Начинки


