from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POMSimple.Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_btn_new_element(self):
        """Da click en el botón mas al inicio de la aplicación"""
        btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, Locators.btn_new_element))
        )
        btn.click()

    def visibility_of_logo(self):
        """Valida que el logo este visible"""
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((MobileBy.XPATH, Locators.logo))
        )
