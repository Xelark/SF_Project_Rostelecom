import time
import pytest
from pages.auth_page import *
from pages.creds import *


def test_positive_registration(browser):
    """Проверка регистрации с валидными данными
    TC-015"""
    # Нажимаем на кнопку Зарегистрироваться:
    page = AuthPage(browser)
    page.reglink()
    browser.implicitly_wait(5)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.input_firstname(reg_firstname)
    browser.implicitly_wait(5)
    # Вводим фамилию:
    page.input_lastname(reg_lastname)
    browser.implicitly_wait(5)
    # Вводим адрес почты или номер телефона:
    page.input_email_or_phone(reg_phone)
    browser.implicitly_wait(5)
    # Вводим пароль:
    page.input_password(reg_pass)
    browser.implicitly_wait(5)
    # Вводим подтверждение пароля:
    page.input_pass_confirm(reg_pass)
    browser.implicitly_wait(5)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()
    # Время для ввода кода подтверждения из почты
    time.sleep(30)

    assert page.get_relative_link() == '/account_b2c/page'


