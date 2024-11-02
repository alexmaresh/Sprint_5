from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import LocatorsStellarBurgers as Locs
from utils import Utils

URL = 'https://stellarburgers.nomoreparties.site/'


# Переход в Личный кабинет
def test_go_from_main_to_lk(driver, get_my_acc):
    driver.get(URL)
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    driver.find_element(*Locs.personal_account_button).click()
    assert driver.current_url == URL + 'login'
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)
    assert driver.current_url == URL + 'account/profile'


# Переход по клику на «Конструктор» из Личного кабинета
def test_go_to_constructor_from_lk_by_label(driver, get_my_acc):
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

    driver.find_element(*Locs.constructor_label).click()
    WebDriverWait(driver, 5).until(
        ec.invisibility_of_element_located(Locs.account_name_input))
    assert driver.current_url == URL


# Переход по клику на логотип Stellar Burgers из ЛК
def test_go_to_constructor_from_lk_by_logo(driver, get_my_acc):
    name, email, password = get_my_acc["name"], get_my_acc["email"], get_my_acc["password"]
    Utils.login(driver, email, password)
    assert Utils.check_auth(driver, name, email)

    driver.find_element(*Locs.header_logo).click()
    WebDriverWait(driver, 5).until(
        ec.invisibility_of_element_located(Locs.account_name_input))

    assert driver.current_url == URL


# Проверь, что работают переходы к разделам: «Булки», «Соусы», «Начинки».
def test_go_to_buns_sauces_fillings(driver):
    driver.get(URL)
    driver.find_element(*Locs.filling_span).click()
    driver.find_element(*Locs.buns_span).click()
    assert 'current' in driver.find_element(*Locs.buns_section).get_attribute('class')
    driver.find_element(*Locs.sauces_span).click()
    assert 'current' in driver.find_element(*Locs.sauces_section).get_attribute('class')
    driver.find_element(*Locs.filling_span).click()
    assert 'current' in driver.find_element(*Locs.filling_section).get_attribute('class')
