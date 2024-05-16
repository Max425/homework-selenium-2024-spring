from ui.pages.base_page import BasePage
from ui.locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    url = 'https://ads.vk.com/hq/registration'

    def click_use_cabinet_myTarget_button(self):
        self.click(RegistrationPageLocators.USE_CABINET_MYTARGET_BUTTON)

    def click_create_new_cabinet_button(self):
        self.click(RegistrationPageLocators.CREATE_NEW_CABINET_BUTTON)

    def change_account_type(self, account_type: str):
        self.click(RegistrationPageLocators.CHANGE_ACCOUNT_TYPE_BUTTON(account_type))

    def is_physical_field_visible(self) -> bool:
        return self.is_visible(RegistrationPageLocators.CHANGE_ACCOUNT_TYPE_BUTTON('Физическое лицо'))

    def change_country(self, country: str):
        self.click(RegistrationPageLocators.CHANGE_COUNTRY)
        self.click(RegistrationPageLocators.CHANGE_COUNTRY_LIST_ITEM(country))

    def change_country_2(self, country: str):
        self.click(RegistrationPageLocators.CHANGE_COUNTRY)
        self.click(RegistrationPageLocators.CHANGE_COUNTRY_LIST_ITEM(country))

    def get_selected_currency(self, currency) -> str:
        self.click(RegistrationPageLocators.CURRENCY)
        return self.find(RegistrationPageLocators.CURRENCY_LIST_ITEM(currency)).text

    def click_submit_button(self):
        self.click(RegistrationPageLocators.SUBMIT_BUTTON)

    def get_error(self) -> str:
        return self.find(RegistrationPageLocators.ERROR_FIELD).text

    def fill_email_field(self, email: str):
        self.fill_field(RegistrationPageLocators.EMAIL_FIELD, email)

    def is_inn_field_visible(self) -> bool:
        return self.is_visible(RegistrationPageLocators.INN_FIELD)

    def fill_inn_field(self, inn: str):
        self.fill_field(RegistrationPageLocators.INN_FIELD, inn)

    def click_offer_field(self):
        self.click(RegistrationPageLocators.OFFER_FIELD)
