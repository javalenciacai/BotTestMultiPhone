from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    time_wait = 30
    """Pasa el tiempo de espera en segundos"""

    def __init__(self, driver):
        """Crear la variable driver"""
        self.driver = driver

    def url(self):
        """Retorna la o las urls de appium o granjas"""
        return 'http://localhost:4723/wd/hub'

    def find_element_validate_clickable(self, element):
        """Busca el elemento por xpath y valida que sea clickable"""
        return WebDriverWait(self.driver, self.time_wait).until(
            EC.element_to_be_clickable((MobileBy.XPATH, element))
        )

    def find_element_validate_visible(self, element):
        """Busca el elemento por xpath y valida que sea clickable"""
        return WebDriverWait(self.driver, self.time_wait).until(
            EC.visibility_of_element_located((MobileBy.XPATH, element))
        )

    def send_keys_to_element(self, element, value):
        """Busca el elemento valida que sea clickable y luego envía el texto"""
        self.find_element_validate_clickable(element).send_keys(value)

    def click_to_element(self, element):
        """Busca el elemento valida que sea clickable y luego da click"""
        self.find_element_validate_clickable(element).click()

    def hide_keyboard(self):
        """Oculta el teclado del teléfono"""
        self.driver.hide_keyboard()
