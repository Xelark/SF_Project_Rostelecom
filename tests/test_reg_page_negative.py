import pytest
from pages.creds import *
from pages.auth_page import *
from pages.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_registration_password_difference(browser):
    """Соответствие паролей в полях ввода 'Пароль' и 'Подтверждение пароля'
    TC-016"""

    page = AuthPage(browser)
    # Переходим к форме регистрации
    page.reglink()
    browser.implicitly_wait(3)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.input_firstname(reg_firstname)
    browser.implicitly_wait(3)
    # Вводим фамилию:
    page.input_lastname(reg_lastname)
    browser.implicitly_wait(3)
    # Вводим адрес почты или телефона:
    page.input_email_or_phone(reg_phone)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.input_password(reg_pass)
    browser.implicitly_wait(3)
    # Вводим отличный от вводимого выше пароля:
    page.input_pass_confirm(wrong_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    # ожидаем, пока появится сообщение о разных паролях
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(*AuthLocators.AUTH_MESS_ERROR))

    error_mess = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_mess.text == 'Пароли не совпадают'


@pytest.mark.parametrize('firstname', [firstname_short, firstname_long, firstname_latin, firstname_digits],
                         ids=['short firstname', 'long firstname', 'latin firstname', 'digits'])
def test_invalid_firstname(browser, firstname):
    """Тест регистрации с неверным форматом поля имени
    TC-017-020"""

    page = AuthPage(browser)
    # Переходим к форме регистрации
    page.reglink()
    browser.implicitly_wait(3)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    # Вводим имя:
    page.input_firstname(reg_firstname)
    browser.implicitly_wait(3)
    # Вводим фамилию:
    page.input_lastname(reg_lastname)
    browser.implicitly_wait(3)
    # Вводим адрес почты или телефона:
    page.input_email_or_phone(reg_phone)
    browser.implicitly_wait(3)
    # Вводим пароль:
    page.input_password(reg_pass)
    browser.implicitly_wait(3)
    # Вводим отличный от вводимого выше пароля:
    page.input_pass_confirm(wrong_password)
    browser.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    page.btn_click()

    # ожидаем, пока появится сообщение о разных паролях
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(*RegLocators.REG_FIRSTNAME_ERROR))

    error_mess = browser.find_element(*RegLocators.REG_FIRSTNAME_ERROR)
    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
