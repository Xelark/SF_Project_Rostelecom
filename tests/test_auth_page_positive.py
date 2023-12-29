import time
import pytest
from pages.auth_page import *
from pages.creds import *


@pytest.mark.parametrize('username', [valid_phone, valid_email, valid_login, valid_account],
                         ids=['phone', 'email', 'login', 'account'])
def test_auth_valid_creds(browser, username):
    """Так как локатор на вкладках для ввода телефона, почты, логина и л/с одинаков,
     мы можем проверить позитивный вход сразу со всеми 4 валидными входными данными кодом 1 теста
     TC-001-004"""
    page = AuthPage(browser)
    page.input_username(username)
    page.input_password(valid_password)
    time.sleep(15)  # Задержка для ввода капчи вручную
    page.btn_click()
    assert page.get_relative_link() == '/account_b2c/page'


def test_reg_page_open(browser):
    """Тест перехода к форме регистрации
    TC-009"""
    page = AuthPage(browser)
    page.reg_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_help_page_open(browser):
    """Тест перехода на страницу помощи
    TC-010"""
    page = AuthPage(browser)
    page.help_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate'


def test_auth_via_vk(browser):
    """Тест авторизации через ВК
    TC-005"""
    page = AuthPage(browser)
    page.vklink()
    assert browser.title == 'ВКонтакте | Вход'
    time.sleep(30) #время для ввода данных аккаунта вк
    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_via_ok(browser):
    """Тест авторизации через ОК
    TC-006"""
    page = AuthPage(browser)
    page.oklink()
    assert browser.title == 'OK'
    time.sleep(30) #время для ввода данных аккаунта ОК
    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_via_mail_ru(browser):
    """Тест авторизации через MAIL.RU
    TC-007"""
    page = AuthPage(browser)
    page.maillink()
    assert browser.title == 'Mail.Ru — Запрос доступа'
    time.sleep(30) #время для ввода данных аккаунта Mail.ru
    assert page.get_relative_link() == '/account_b2c/page'


def test_auth_via_ya(browser):
    """Тест авторизации через Яндекс
    TC_008"""
    page = AuthPage(browser)
    page.yalink()
    assert browser.title == 'Авторизация'
    time.sleep(30) #время для ввода данных аккаунта Yandex
    assert page.get_relative_link() == '/account_b2c/page'
