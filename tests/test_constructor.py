from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructor:

    def test_sauces_scroll_to_sauces_section(self, driver, login):

        sauces_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES_TAB))
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        driver.execute_script("arguments[0].click();", sauces_tab)
        sauces_title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCES_SECTION_TITLE))
        assert sauces_title.text == "Соусы"


    def test_buns_scroll_to_buns_section(self, driver, login):
        buns_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS_TAB))
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)

        buns_title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS_SECTION_TITLE))
        assert buns_title.text == "Булки"


    def test_fillings_scroll_to_fillings_section(self, driver, login):
        fillings_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FILLINGS_TAB))
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        driver.execute_script("arguments[0].click();", fillings_tab)

        fillings_title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION_TITLE))
        assert fillings_title.text == "Начинки"