import pytest
from selenium import webdriver
from random import randint

NAME = "al_maresh_15"
MAIL = "@yandex.ru"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def get_correct_acc():
    params = {
        "name": NAME,
        "email": NAME + f"_{randint(100, 1000)}" + MAIL,
        "password": str(randint(100000, 999999)),
    }
    yield params

@pytest.fixture()
def get_incorrect_pass():
    params = {
        "name": NAME,
        "email": NAME + f"_{randint(100, 1000)}" + MAIL,
        "password": str(randint(10000, 99999)),
    }
    yield params

'''Конечно, хранить данные в коде никто не будет и в не-учебном проекте их нужно убрать в .env'''
@pytest.fixture()
def get_my_acc():
    params = {
        "name": "alex",
        "email": "al_maresh_15_024@ya.ru",
        "password": str(12345678)
    }
    yield params