from selenium.webdriver.common.by import By


class Locators:

    ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    REG_LINK = [By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a"]
    USER_NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    PASSWORD = (By.XPATH, "//input[@name= 'Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p")

    ENTER_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    ENTER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/div/form/button")
    MAKE_ORDER_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button")
    ENTER_LINK = (By.XPATH, "// *[ @ id = 'root'] / div / main / div / div / p / a")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a")

