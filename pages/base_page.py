from pages.creds import URL
from urllib.parse import urlparse

class BasePage(object):
   # конструктор класса - специальный метод с ключевым словом __init__
   # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
   def __init__(self, driver, timeout=10):
       self.driver = driver
       self.url = URL
       self.driver.implicitly_wait(timeout)


   def get_relative_link(self):
       url = urlparse(self.driver.current_url)
       return url.path