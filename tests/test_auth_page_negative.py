#import time
import pytest
from pages.auth_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.creds import *


@pytest.mark.parametrize('username', [wrong_phone, wrong_email, wrong_login, wrong_account],
                         ids=['wrong phone', 'wrong email', 'wrong login', 'wrong account'])
def test_wrong_creds_and_error_message(browser, username):
    """В данном тесте проверяются пары неверных типов логинов + неверный пароль,
    а также появления сообщения об ошибке авторизации
    TC-011-014"""
    page = AuthPage(browser)
    page.input_username(username)
    page.input_password(wrong_password)
    page.btn_click()
    #ожидаем, пока появится сообщение о неверных данных
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located(*AuthLocators.AUTH_FORM_ERROR))

    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)

    assert error_message.text == 'Неверный логин или пароль'
