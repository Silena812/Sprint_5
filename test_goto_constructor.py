from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *

class TestGoToConstructor:

    def test_goto_constructor_main_site_opened(self, driver, login):

        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

class TestGoToConstructorLogo:

    def test_goto_constructor_logo_main_site_opened(self, driver, login):

        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site