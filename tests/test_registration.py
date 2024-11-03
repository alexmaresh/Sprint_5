from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import LocatorsStellarBurgers as Locs
from utils import Utils

URL = 'https://stellarburgers.nomoreparties.site/'

#Успешная регистрация
def test_successful_registration(driver, get_correct_acc):
    driver.get(URL + 'register')
    name, email, password = get_correct_acc["name"], get_correct_acc["email"], get_correct_acc["password"]
    Utils.register(driver, name, email, password)
    WebDriverWait(driver, 5).until(ec.invisibility_of_element_located(Locs.button_reg))
    assert driver.current_url == URL + 'login'

#Неуспешная регистрация с неверным паролем
def test_failed_registration_incorrect_password(driver, get_incorrect_pass):
    driver.get(URL + 'register')
    name, email, password = get_incorrect_pass["name"], get_incorrect_pass["email"], get_incorrect_pass["password"]
    Utils.register(driver, name, email, password)
    WebDriverWait(driver, timeout=10).until(ec.visibility_of_element_located(Locs.error_reg))
    error_text = driver.find_element(*Locs.error_reg).text
    assert error_text == 'Некорректный пароль'
