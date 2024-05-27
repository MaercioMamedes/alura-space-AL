from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from django.contrib.auth.models import User


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
        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")

        username_input.send_keys("teste")
        password_input.send_keys("1234")

        button_login = self.selenium.find_element(By.XPATH,  "/html/body/div/main/section[2]/section/form/div[2]/button")

        button_login.click()

        result = self.selenium.find_element(By.XPATH, "/html/body/div/div")

        self.assertEquals(result.text, "teste logado com sucesso")
