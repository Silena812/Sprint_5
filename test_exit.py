from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *

class TestExitAccount:

    def test_exit_account_main_site_opened(self, driver, login):

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))
        assert driver.current_url == login_site