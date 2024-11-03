from locators import LocatorsStellarBurgers as Locs
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Utils:
    @staticmethod
    def login(driver, email, password):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*Locs.login_email).send_keys(email)
        driver.find_element(*Locs.login_password).send_keys(password)
        driver.find_element(*Locs.login_button).click()
        WebDriverWait(driver, 5).until(
            ec.invisibility_of_element_located(Locs.login_button))

    @staticmethod
    def register(driver, name, email, password):
        driver.find_element(*Locs.reg_name_input).send_keys(name)
        driver.find_element(*Locs.reg_email_input).send_keys(email)
        driver.find_element(*Locs.reg_password_input).send_keys(password)
        driver.find_element(*Locs.button_reg).click()

    @staticmethod
    def check_auth(driver, name, email):
        driver.find_element(*Locs.personal_account_button).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(Locs.account_name_input))
        assert driver.find_element(*Locs.account_name_input).get_attribute("value") == name
        assert driver.find_element(*Locs.account_email_input).get_attribute("value") == email
        return True
