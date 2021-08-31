import unittest

import pytest
from appium import webdriver
from POMSimple.Pages.loginPage import LoginPage
from POMSimple.Pages.homePage import HomePage
import time
from Resource.devices import Devices


class TestLogin(unittest.TestCase):
    param = None
    driver = None

    def setUp(self):
        self.driver = webdriver.Remote(
            "http://006f3e1f30d3b6e8bd23589408c34392:924543c91cb9a87429f355933cf35d08@hub.testingbot.com/wd/hub",
            Devices.galaxyS8Virtual)

    @pytest.mark.login
    def test_login_with_incorrect_username(self):
        login = LoginPage(self.driver)
        login.enter_username("administrador_devaaaa@automata.com")
        login.enter_password("1111")
        login.click_login()
        login.validate_message_username_incorrect()

    @pytest.mark.skip
    def test_login_with_incorrect_password(self):
        login = LoginPage(self.driver)
        login.enter_username("administrador_dev@automata.com")
        login.enter_password("2222")
        login.click_login()
        login.validate_message_password_incorrect()

    @pytest.mark.skip
    def test_login_with_correct_credentials(self):
        login = LoginPage(self.driver)
        login.enter_username("administrador_dev@automata.com")
        login.enter_password("1111")
        login.click_login()

        homepage = HomePage(self.driver)
        homepage.visibility_of_logo()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


"""
        txt_user = "//android.widget.EditText[contains(@text, 'Email')]"
        txt_password = "//android.widget.EditText[contains(@text, 'Contraseña')]"
        btn_login = "//android.widget.TextView[contains(@text, 'INGRESAR')]"
        btn_New_Element = "//android.widget.TextView[contains(@text, '')]"
        link_company = "//android.widget.TextView[contains(@text, 'Segundaempresaautomataprod')]"
        
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(txt_user).send_keys("javalenciacai@gmail.com")
        
        txtUser = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((MobileBy.XPATH, txt_user))
        )
        txtUser.send_keys("administrador_dev@automata.com")
    
        txtPassword = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, txt_password))
        )
        txtPassword.send_keys("1111")
    
        btnLogin = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, btn_login))
        )
    
        btnLogin.click()
    
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((MobileBy.XPATH, btn_New_Element))
        )
    
        linkCompany = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, link_company))
        )
    
        linkCompany.click()
    
        driver.quit()
"""
