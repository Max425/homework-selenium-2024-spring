from selenium.webdriver.common.by import By


class SettingsAccessPageLocators:
    MORE_HREF = (By.XPATH, f"//*[@href='/help/articles/additionalaccounts']")

    ADD_CABINET_BUTTON = (By.XPATH, f"//*[@data-testid='add-user']")

    SAVE_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Сохранить']")
