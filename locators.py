from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    ACCOUNT = (By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    REG_LINK = [By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a"]
    REG_NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")
    REG_EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    REG_PASSWORD = (By.XPATH, "//input[@name= 'Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")


