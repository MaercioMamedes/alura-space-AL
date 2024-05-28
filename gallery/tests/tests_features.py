from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User
import time

class MySeleniumTests(StaticLiveServerTestCase):

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
        cls.selenium = WebDriver()
        # cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        self._findByName("username").send_keys("teste")
        self._findByName("password").send_keys("1234")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "teste logado com sucesso")

    def test_invalid_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        
        self._findByName("username").send_keys("invalid_username")
        self._findByName("password").send_keys("invalid_password")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "Usuário ou senhas inválidos")
    
    def test_register(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/register'))

        self._findById("id_first_name").send_keys("Jhon")
        self._findById("id_last_name").send_keys("Due")
        self._findById("id_username").send_keys("jhon_due")
        self._findById("id_email").send_keys("jhon_due@gmail.com")
        self._findById("id_password").send_keys("~çsiA1203#%&1")
        self._findById("id_password_confirm").send_keys("~çsiA1203#%&1")

        self._findBySelector("body > div > main > section.galeria > form > div:nth-child(3) > button").click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "cadastro realizado com sucesso")

    def test_logout(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/users/login'))
        
        self._findByName("username").send_keys("teste")
        self._findByName("password").send_keys("1234")

        self._findByXpath("/html/body/div/main/section[2]/section/form/div[2]/button").click()
        self._findByXpath('//a[@href="/users/logout"]').click()

        self.assertEqual(self._findByXpath("/html/body/div/div").text, "logout realizado com sucesso")

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
