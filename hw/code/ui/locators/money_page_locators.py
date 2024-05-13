from selenium.webdriver.common.by import By


class MoneyPageLocators:
    TITLE = (By.XPATH, "//*[contains(@class, 'PartnerContent_title__')]")
    SUBTITLE = (By.XPATH, "//*[contains(@class, 'PartnerContent_description__')]")

    CABINET_BUTTON = (By.XPATH, "//*[contains(@class, 'PartnerContent_headerButton__')]")
    HELP_BUTTON = (By.XPATH, "//*[contains(@class, 'PartnerContent_headerButtonSecondary__')]")

    SITE_BUTTON = (By.XPATH, f"//*[contains(@class, 'Tabs_tab__') and text()='Для сайтов']")
    APP_BUTTON = (By.XPATH, f"//*[contains(@class, 'Tabs_tab__') and text()='Для сайтов']")

    @staticmethod
    def GOODS_ITEM_TITLE(item_name):
        return By.XPATH, f"//*[contains(@class, 'Slider_title__') and text()='{item_name}']"

    @staticmethod
    def FORMAT_ITEM_TITLE(item_name):
        return By.XPATH, f"//*[contains(@class, 'Slider_title__') and text()='{item_name}']"

    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'Form_button__')]")
    SUBMIT_MESSAGE = (By.XPATH, "//*[contains(@class, 'Form_success__')]")
