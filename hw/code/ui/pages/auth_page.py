from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators
import time


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)

        login_input = self.find(self.locators.LOGIN_FIElD)
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.NEXT_BUTTON)

        password_input = self.find(self.locators.PASSWORD_FIELD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BUTTON)
        