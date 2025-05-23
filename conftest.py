import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.headless = False
    service = Service()
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(main_site)
    yield browser
    browser.quit()



@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON_MAIN).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.ENTER_BUTTON)
    )
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.ENTER_BUTTON).click()

    return driver

