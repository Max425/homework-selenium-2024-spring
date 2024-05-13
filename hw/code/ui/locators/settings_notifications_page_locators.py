from selenium.webdriver.common.by import By


class SettingsNotificationsPageLocators:
    EMAIL_CHECKBOX = (By.XPATH, f"//*[@class='vkuiSwitch__pseudo']")

    SAVE_BUTTON = (By.XPATH, f"//*[@data-testid='settings-save']")

    CANCEL_BUTTON = (By.XPATH, f"//*[@data-testid='settings-cancel']")

    @staticmethod
    def SELECT_NOTIFICATION_SETTING(select_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__title')]//div[text()='{select_type}']"
    