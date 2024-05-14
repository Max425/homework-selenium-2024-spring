from selenium.webdriver.common.by import By


class SettingsNotificationsPageLocators:
    EMAIL_CHECKBOX = (By.XPATH, f"//*[@class='vkuiSwitch__pseudo']")

    SAVE_BUTTON = (By.XPATH, f"//*[@data-testid='settings-save']")

    CANCEL_BUTTON = (By.XPATH, f"//*[@data-testid='settings-cancel']")

    @staticmethod
    def SELECT_NOTIFICATION_SETTING(select_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__title')]//div[text()='{select_type}']"
    
    PHONE_INPUT = (By.XPATH, f"//*[@data-testid='general-phone']")
    INN_INPUT = (By.XPATH, f"//*[@data-testid='general-ord-inn']")
    ADD_EMAIL_BTN = (By.XPATH, f"//*[@data-testid='add-email']")
    ADD_EMAIL_INPUT = (By.XPATH, f"//*[@data-testid='email-0']")
    
    