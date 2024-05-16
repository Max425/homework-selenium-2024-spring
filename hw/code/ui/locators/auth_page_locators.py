from selenium.webdriver.common.by import By


class AuthPageLocators:
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    LOGIN_FIElD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, "password")
    NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")
