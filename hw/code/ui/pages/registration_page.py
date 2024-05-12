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

    def get_selected_language(self) -> str:
        return self.find(RegistrationPageLocators.SELECTED_LANGUAGE).text

    def select_language(self, language: str):
        self.click(RegistrationPageLocators.LANGUAGE_BUTTON(language))

    def select_country(self, country_name: str):
        self.click(RegistrationPageLocators.COUNTRY_DROPDOWN)
        self.click(RegistrationPageLocators.COUNTRY_DROPDOWN_ITEM(country_name))

    def currency_dropdown_contain_items(self, item_names: list):
        self.click(RegistrationPageLocators.CURRENCY_DROPDOWN)
        for item_name in item_names:
            item = self.find(RegistrationPageLocators.CURRENCY_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

            return True

    def click_submit_button(self):
        self.scroll_and_click(RegistrationPageLocators.SUBMIT_BUTTON)

    def get_email_error(self) -> str:
        return self.find(RegistrationPageLocators.EMAIL_ERROR).text

    def get_inn_error(self) -> str:
        return self.find(RegistrationPageLocators.INN_ERROR).text

    def get_offer_error(self) -> str:
        return self.find(RegistrationPageLocators.OFFER_ERROR).text

    def click_offer_checkbox(self):
        self.scroll_and_click(RegistrationPageLocators.OFFER_CHECKBOX)

    def enter_email(self, email: str):
        elem = self.find(RegistrationPageLocators.EMAIL_INPUT)
        elem.clear()
        elem.send_keys(email)

    def enter_inn(self, inn: str):
        elem = self.find(RegistrationPageLocators.INN_INPUT)
        elem.clear()
        elem.send_keys(inn)

    def physical_type_became_invisible(self) -> bool:
        return self.became_invisible(RegistrationPageLocators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))

    def physical_type_became_visible(self) -> bool:
        return self.became_visible(RegistrationPageLocators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))