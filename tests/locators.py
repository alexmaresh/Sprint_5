from selenium.webdriver.common.by import By


class LocatorsStellarBurgers:
    # personal account
    # personal_account_button = By.XPATH, "//p[text() = 'Личный Кабинет']"
    personal_account_button = By.XPATH, "//*[@id='root']/div/header/nav/a/p[text()='Личный Кабинет']"
    account_name_input = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[1]//input"
    account_email_input = By.XPATH, "//ul[@class = 'Profile_profileList__3vTor' ]/li[2]//input"

    # registration
    register = By.XPATH, "//a[@href = '/register']"
    reg_name_input = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input"
    reg_email_input = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input"
    reg_password_input = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[3]//input"
    button_reg = By.XPATH, "//button[text()='Зарегистрироваться']"
    error_reg = By.XPATH, "//p[@class = 'input__error text_type_main-default']"

    # auth
    login_button = By.XPATH, "//button[text()='Войти']"
    logout_button = By.XPATH, "//button[text()='Выход']"

    login_enter_button = By.XPATH, "//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']"
    login_enter_label = By.XPATH, "//a[@class = 'Auth_link__1fOlj']"

    login_email = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[1]//input"
    login_password = By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20' ]//fieldset[2]//input"

    # constructor
    constructor_label = By.XPATH, "//p[text() = 'Конструктор' ]"
    header_logo = By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2' ]"

    buns_span = By.XPATH, "//span[text()='Булки']"
    buns_section = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[1]"

    sauces_span = By.XPATH, "//span[text()='Соусы']"
    sauces_section = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[2]"

    filling_span = By.XPATH, "//span[text()='Начинки']"
    filling_section = By.XPATH, "//section[@class = 'BurgerIngredients_ingredients__1N8v2']/div/div[3]"
