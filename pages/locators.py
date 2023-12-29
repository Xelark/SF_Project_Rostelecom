from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы на странице авторизации"""
    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.CLASS_NAME, 'kc-login')
    AUTH_FORGOT_PASS = (By.ID, 'forgot_password')
    AUTH_LINK_REG = (By.ID, 'kc-register')
    AUTH_HELP = (By.XPATH, "//*[@id='faq-open']/a")
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_MESS_ERROR = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[4]/div[2]/span")
    AUTH_VIA_VK = (By.ID, 'oidc_vk')
    AUTH_VIA_OK = (By.ID, 'oidc_ok')
    AUTH_VIA_MAIL = (By.ID, 'oidc_mail')
    AUTH_VIA_YANDEX = (By.ID, 'oidc_ya')


class RegLocators:
    """Локаторы на странице регистрации"""
    REG_FIRSTNAME = (By.NAME, 'firstName')
    REG_LASTNAME = (By.NAME, 'lastName')
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_MAIL_OR_PHONE = (By.ID, 'address')
    REG_PASS = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.ID, 'password-confirm')
    REG_REGISTER = (By.XPATH, "//button[@name='register']")
    REG_FIRSTNAME_ERROR = (By.XPATH, "//*[@id='page-right']/div/div[1]/div/form/div[1]/div[1]/span")
