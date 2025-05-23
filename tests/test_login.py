from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Credentials
from curl import *

class TestEnterAccountButtonMainPage:

    def test_enter_account_main_page_valid_credentials_account_opened(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == main_site

class TestEnterAccountButtonAccount:

    def test_enter_account_account_page_valid_credentials_account_opened(self, driver):

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == main_site

class TestEnterAccountButtonRegistrationForm:

    def test_enter_account_registration_form_valid_credentials_account_opened(self, driver):

        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.ENTER_LINK).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == main_site

class TestEnterAccountButtonForgotPassword:

    def test_enter_account_forgot_password_valid_credentials_account_opened(self, driver):

        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON_MAIN).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*Locators.ENTER_LINK).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.ENTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

        assert driver.current_url == main_site