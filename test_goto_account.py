from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *

class TestGoToAccount:

    def test_goto_account_account_opened(self, driver, login):

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(account_site))

        assert driver.current_url == account_site
