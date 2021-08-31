from POMSimple.Locators.locators import Locators
from Base.Page import Page


class LoginPage(Page):
    def __init__(self, driver):
        Page.__init__(self, driver)
        self.page = Page(driver)

    def enter_username(self, username):
        """Digita el usuario"""
        self.page.send_keys_to_element(Locators.txt_user, username)

    def enter_password(self, password):
        """Digita la contraseña"""
        self.page.send_keys_to_element(Locators.txt_password, password)

    def click_login(self):
        """Da click en el botón ingresar"""
        self.page.click_to_element(Locators.btn_login)

    def validate_message_username_incorrect(self):
        """Valida que muestre el mensaje de que el usuario es incorrecto"""
        self.page.find_element_validate_visible(Locators.lbl_username_incorrect)


    def validate_message_password_incorrect(self):
        """Valida que muestre el mensaje de que el usuario es incorrecto"""
        self.page.find_element_validate_visible(Locators.lbl_password_incorrect)
