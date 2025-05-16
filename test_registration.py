from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from helper import generate_wrong_password
from helper import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver):

        email, password, username = generate_registration_data()
        print("Открыта главная страница")
        driver.find_element(*Locators.ACCOUNT).click()
        print("Клик на 'Личный кабинет'")
        driver.find_element(*Locators.REG_LINK).click()
        print("Клик на 'Зарегистрироваться'")
        driver.find_element(*Locators.REG_NAME).send_keys(username)
        print("Введено имя")
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        print("Введён email")
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        print("Введён пароль")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        print("Клик на кнопку регистрации")
        print(f"Текущий URL: {driver.current_url}")

        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))
        print(f"Текущий URL: {driver.current_url}")
        assert driver.current_url == login_site


class TestRegistrationWithInvalidPassword:

    def test_registration_invalid_password_error_message(self, driver):

        email, password, username = generate_wrong_password()
        print("Открыта главная страница")
        driver.find_element(*Locators.ACCOUNT).click()
        print("Клик на 'Личный кабинет'")
        driver.find_element(*Locators.REG_LINK).click()
        print("Клик на 'Зарегистрироваться'")
        driver.find_element(*Locators.REG_NAME).send_keys(username)
        print("Введено имя")
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        print("Введён email")
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        print("Введён пароль")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        print("Клик на кнопку регистрации")
        print(f"Текущий URL: {driver.current_url}")
        wrong_pw_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_MESSAGE)).text
        print(f"Текущий URL: {driver.current_url}")
        print("Сообщение об ошибке:", wrong_pw_message)
        assert driver.current_url == main_site + 'register'
        assert wrong_pw_message == 'Некорректный пароль'

class TestRegistrationWithEmptyPassword:

    def test_registration_empty_password_no_message(self, driver):

        email, password, username = generate_wrong_password()
        print("Открыта главная страница")
        driver.find_element(*Locators.ACCOUNT).click()
        print("Клик на 'Личный кабинет'")
        driver.find_element(*Locators.REG_LINK).click()
        print("Клик на 'Зарегистрироваться'")
        driver.find_element(*Locators.REG_NAME).send_keys(username)
        print("Введено имя")
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        print("Введён email")
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        print("Введён пароль")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        print("Клик на кнопку регистрации")
        print(f"Текущий URL: {driver.current_url}")

        assert driver.current_url == main_site + 'register'
