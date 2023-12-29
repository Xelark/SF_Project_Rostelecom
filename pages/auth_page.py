from .base_page import BasePage
from .locators import AuthLocators, RegLocators
import time
import os

class RegPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        #создаем элементы страницы
        self.first_name = driver.find_element(*RegLocators.REG_FIRSTNAME)
        self.last_name = driver.find_element(*RegLocators.REG_LASTNAME)
        self.email = driver.find_element(*RegLocators.REG_MAIL_OR_PHONE)
        self.password = driver.find_element(*RegLocators.REG_PASS)
        self.pass_conf = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_REGISTER)

    def input_firstname(self, value):
        self.first_name.send_keys(value)

    def input_lastname(self, value):
        self.last_name.send_keys(value)

    def input_email_or_phone(self, value):
        self.email.send_keys(value)

    def input_password(self, value):
        self.password.send_keys(value)

    def input_pass_confirm(self, value):
        self.pass_conf.send_keys(value)

    def btn_click(self):
        self.btn.click()

class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
        #создаем элементы страницы
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.reglink = driver.find_element(*AuthLocators.AUTH_LINK_REG)
        self.helplink = driver.find_element(*AuthLocators.AUTH_HELP)
        self.vklink = driver.find_element(*AuthLocators.AUTH_VIA_VK)
        self.oklink = driver.find_element(*AuthLocators.AUTH_VIA_OK)
        self.maillink = driver.find_element(*AuthLocators.AUTH_VIA_MAIL)
        self.yalink = driver.find_element(*AuthLocators.AUTH_VIA_YANDEX)
        time.sleep(3)

    def input_username(self, value):
        self.username.send_keys(value)

    def input_password(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
        time.sleep(3) #ждем реакции

    def reg_click(self):
        self.reglink.click()
        time.sleep(10) #ждем открытия формы регистрации

    def help_click(self):
        self.helplink.click()
        time.sleep(3) #ждем открытия страницы помощи

    def vk_click(self):
        self.vklink.click()
        time.sleep(3) #ждем открытия авторизации через ВКкон

    def ok_click(self):
        self.oklink.click()
        time.sleep(3) #ждем открытия авторизации через ОК

    def mail_ru_click(self):
        self.maillink.click()
        time.sleep(3) #ждем открытия авторизации через Мейл.Ру

    def ya_click(self):
        self.yalink.click()
        time.sleep(3) #ждем открытия авторизации через Яндекс



