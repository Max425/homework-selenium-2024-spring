from ui.locators.auth_page_locators import AuthPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class AuthPage(BasePage):
    locators = AuthPageLocators()
    
    def login(self, login, password):
        self.click(AuthPageLocators.MAIL_RU_AUTH_BUTTON)

        login_input = self.find(AuthPageLocators.LOGIN_FIElD)
        login_input.clear()
        login_input.send_keys(login)

        self.click(AuthPageLocators.NEXT_BUTTON)

        password_input = self.find(AuthPageLocators.PASSWORD_FIELD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BUTTON)
        self.find(locator=(By.ID, "header")) # ждем рендера страницы