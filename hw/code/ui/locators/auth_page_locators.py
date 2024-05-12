from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    LOGIN_FIElD = (By.NAME, 'username')
    PASSWORD = (By.NAME, "password")
    NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")