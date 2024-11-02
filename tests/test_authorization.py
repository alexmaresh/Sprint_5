from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import LocatorsStellarBurgers as Locs
from utils import Utils

URL = 'https://stellarburgers.nomoreparties.site/'

#вход по кнопке «Войти в аккаунт» на главной
def test_login_account_button_main(driver, get_my_acc):
    driver.get(URL)
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    driver.find_element(*Locs.login_enter_button).click()
    assert driver.current_url == URL + 'login'
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

#Вход через кнопку «Личный кабинет»
def test_login_button_lk(driver, get_my_acc):
    driver.get(URL)
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    driver.find_element(*Locs.personal_account_button).click()
    assert driver.current_url == URL + 'login'
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

#Вход через кнопку в форме регистрации
def test_login_registration_form(driver, get_my_acc):
    driver.get(URL + 'register')
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    driver.find_element(*Locs.login_enter_label).click()
    WebDriverWait(driver, 5).until(ec.invisibility_of_element_located(Locs.button_reg))
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

#Вход через кнопку в форме восстановления пароля
def test_login_forgot_password(driver, get_my_acc):
    driver.get(URL + 'forgot-password')
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    driver.find_element(*Locs.login_enter_label).click()
    WebDriverWait(driver, 5).until(
        ec.visibility_of_element_located(Locs.login_button))
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

#Выход по кнопке «Выйти» в личном кабинете.
def test_logout_button_lk(driver, get_my_acc):
    driver.get(URL + 'login')
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)
    driver.find_element(*Locs.logout_button).click()
    WebDriverWait(driver, 5).until(
        ec.invisibility_of_element_located(Locs.account_name_input))
    assert driver.current_url == URL + 'login'

