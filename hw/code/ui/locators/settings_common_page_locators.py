from selenium.webdriver.common.by import By


class SettingsCommonPageLocators:
    SAVE_BUTTON = (By.XPATH, f"//*[@data-testid='settings-save']")

    CANCEL_BUTTON = (By.XPATH, f"//*[@data-testid='settings-cancel']")

    PHONE_INPUT = (By.XPATH, f"//*[@data-testid='general-phone']")
    INN_INPUT = (By.XPATH, f"//*[@data-testid='general-ord-inn']")
    ADD_EMAIL_BTN = (By.XPATH, f"//*[@data-testid='add-email']")
    ADD_EMAIL_INPUT = (By.XPATH, f"//*[@data-testid='email-0']")
    NAME_INPUT = (By.XPATH, f"//*[@data-testid='general-ord-name']")

    ADD_MY_TARGET_CABINET = (
    By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Привязать кабинет myTarget']")
    ADDIING_MY_TARGET_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalCardBase__container')]")

    ADD_API = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Запросить доступ к API']")
    ADDIING_API_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalPage__in-wrap')]")

    CANSEL_ADDING_EMAIL = (By.XPATH, f"//*[@aria-label='Удалить']")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")
