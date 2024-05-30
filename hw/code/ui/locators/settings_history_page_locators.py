from selenium.webdriver.common.by import By


class SettingsHistoryPageLocators:
    FILTER_BUTTON = (By.XPATH, f"//*[@data-testid='filter-button']")

    SAVE_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Применить']")

    CANCEL_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Отмена']")

    CANCEL_DATA_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Отменить']")

    @staticmethod
    def SELECT_FILTER_FIELD(filter):
        return By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='{filter}']"

    @staticmethod
    def CHECK_FILTER_FIELD(filter):
        return By.XPATH, f"//*[contains(@class, 'vkuiTypography')]//div[text()='{filter}']"

    FILTER_DATA_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiIcon--calendar_outline_24')]")

    @staticmethod
    def SELECT_FILTER_DATA_FIELD(filter):
        return By.XPATH, f"//*[contains(@class, 'rdrStaticRangeLabel') and text()='{filter}']"
