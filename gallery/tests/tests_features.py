import socket
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.auth.models import User
from django.test import override_settings, tag

@override_settings(ALLOWED_HOSTS=['*'])
class MySeleniumTests(StaticLiveServerTestCase):
    host = '0.0.0.0'

    def setUp(self):
        user = User.objects.create_user(
            username='teste',
            email='teste@teste.com'
        )

        user.set_password('1234')
        user.save()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.host = socket.gethostbyname(socket.gethostname())
        time.sleep(1)
        cls.selenium = webdriver.Remote(command_executor='http://selenium:4444/wd/hub', options=webdriver.ChromeOptions())

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        self._sendKeysByName("username", "teste")
        self._sendKeysByName("password", "1234")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "teste logado com sucesso")

    def test_invalid_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        
        self._sendKeysByName("username", "invalid_username")
        self._sendKeysByName("password", "invalid_password")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "Usuário ou senhas inválidos")
    
    def test_register(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/register'))

        self._sendKeysById("id_first_name", "Jhon")
        self._sendKeysById("id_last_name", "Due")
        self._sendKeysById("id_username", "jhon_due")
        self._sendKeysById("id_email", "jhon_due@gmail.com")
        self._sendKeysById("id_password", "~çsiA1203#%&1")
        self._sendKeysById("id_password_confirm", "~çsiA1203#%&1")

        self._findBySelector("body > div > main > section.galeria > form > div:nth-child(3) > button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "cadastro realizado com sucesso")

    def test_logout(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        
        self._sendKeysByName("username", "teste")
        self._sendKeysByName("password", "1234")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()
        self._findByXpath('//a[@href="/users/logout"]').click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "logout realizado com sucesso")

    def _sendKeysByName(self, element: str, value: str):
        return self._findByName(element).send_keys(value)

    def _sendKeysById(self, element: str, value: str):
        return self._findById(element).send_keys(value)

    def _findById(self, element: str):
        return self._findElementBy(By.ID, element)

    def _findByName(self, element: str):
        return self._findElementBy(By.NAME, element)
    
    def _findByXpath(self, element: str):
        return self._findElementBy(By.XPATH, element)
    
    def _findBySelector(self, element: str):
        return self._findElementBy(By.CSS_SELECTOR, element)

    def _findByClass(self, element: str):
        return self._findElementBy(By.CLASS_NAME, element)

    def _findElementBy(self, by: By, element: str):
        return self.selenium.find_element(by, element)
