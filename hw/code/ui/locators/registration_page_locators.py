from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    USE_CABINET_MYTARGET_BUTTON = (By.ID, "click-exportMTButton")

    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    @staticmethod
    def CHANGE_ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//span[text()='{account_type}']"
    
    CHANGE_COUNTRY = (By.XPATH, f"//*[@data-testid='country']")

    @staticmethod
    def CHANGE_COUNTRY_LIST_ITEM(country):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{country}']"

    CURRENCY = (By.XPATH, f"//*[@data-testid='currency']")

    @staticmethod
    def CURRENCY_LIST_ITEM(currency):
        return By.XPATH, f"//*[@title='{currency}']"
    
    SUBMIT_BUTTON = (By.XPATH, f"//*[@data-testid='create-button']")

    ERROR_FIELD = (By.XPATH, f"//*[@role='alert']")

    EMAIL_FIELD = (By.XPATH, f"//*[@data-testid='email']")
    
    INN_FIELD = (By.NAME, "inn")

    OFFER_FIELD = (By.NAME, "offer")