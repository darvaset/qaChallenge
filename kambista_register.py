# coding=utf-8
import unittest
from selenium import webdriver
from register import RegisterPage
from data import TestData

class KambistaRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicia una sesión de Firefox y maximiza la ventana
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

        # Navega a la página web requerida
        cls.driver.get('localhost:4000')

    def test_001_login_page(self):
        # Define el nevegador a la variable driver
        driver = self.driver

        #Valida que el título de la página sea correcto
        self.assertEqual('Kambista', driver.title)

    def test_002_tc01(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email('')
        register.enter_password('')
        register.click_register_button()

        # Campos vacíos deberían mostrar REQUIRED
        self.assertIn('REQUIRED', driver.page_source)

    def test_003_tc02(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email('')
        register.enter_password(TestData.validPassword)
        register.click_register_button()

        # Campos vacíos deberían mostrar REQUIRED
        self.assertIn('REQUIRED', driver.page_source)

    def test_004_tc03(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email(TestData.validUser)
        register.enter_password('')
        register.click_register_button()

        # Campos vacíos deberían mostrar REQUIRED
        self.assertIn('REQUIRED', driver.page_source)

    def test_005_tc04(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email(TestData.invalidUser)
        register.enter_password(TestData.invalidPassword)
        register.click_register_button()

        # Usario y Password invalidos
        self.assertIn('INVALID', driver.page_source)

    def test_006_tc05(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email(TestData.invalidUser)
        register.enter_password(TestData.validPassword)
        register.click_register_button()

        # Usario invalido pero Password valido
        self.assertIn('INVALID', driver.page_source)

    def test_007_tc06(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email(TestData.validUser)
        register.enter_password(TestData.invalidPassword)
        register.click_register_button()

        # Usario valido pero Password invalido
        self.assertIn('INVALID', driver.page_source)

    def test_007_tc06(self):
        driver = self.driver
        register = RegisterPage(driver)

        register.enter_email(TestData.validUser)
        register.enter_password(TestData.validPassword)
        register.click_register_button()

        # Usario y Password validos, debería mostrar SAVED
        self.assertIn('SAVED', driver.page_source)

    @classmethod
    def tearDownClass(cls):
        # Cierra la sesión de Firefox
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)
