from ui.pages.base_page import BasePage
from ui.locators.settings_common_page_locators import SettingsCommonPageLocators


class SettingsCommonPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'

    def click_save_button(self):
        self.click(SettingsCommonPageLocators.SAVE_BUTTON)

    def is_save_button_visible(self) -> bool:
        return self.is_visible(SettingsCommonPageLocators.SAVE_BUTTON)

    def is_save_button_enabled(self) -> bool:
        return self.find(SettingsCommonPageLocators.SAVE_BUTTON).is_enabled()

    def click_cancel_button(self):
        self.click(SettingsCommonPageLocators.CANCEL_BUTTON)

    def enter_phone_number(self, phone: str):
        input = self.find(SettingsCommonPageLocators.PHONE_INPUT)
        input.clear()
        input.send_keys(phone)

    def enter_email(self, email: str):
        input = self.find(SettingsCommonPageLocators.ADD_EMAIL_INPUT)
        input.clear()
        input.send_keys(email)

    def enter_inn(self, inn: str):
        input = self.find(SettingsCommonPageLocators.INN_INPUT)
        input.clear()
        input.send_keys(inn)

    def enter_name(self, name: str):
        input = self.find(SettingsCommonPageLocators.NAME_INPUT)
        input.clear()
        input.send_keys(name)

    def click_add_email_button(self):
        self.click(SettingsCommonPageLocators.ADD_EMAIL_BTN)

    def click_close_email_button(self):
        self.click(SettingsCommonPageLocators.CANSEL_ADDING_EMAIL)

    def is_email_input_visible(self) -> bool:
        return self.is_visible(SettingsCommonPageLocators.ADD_EMAIL_INPUT)

    def get_error_text(self) -> str:
        return self.find(SettingsCommonPageLocators.ERROR_MESSAGE).text

    def is_error_visible(self) -> bool:
        return self.is_visible(SettingsCommonPageLocators.ERROR_MESSAGE)

    def click_add_my_target_button(self):
        self.click(SettingsCommonPageLocators.ADD_MY_TARGET_CABINET)

    def is_adding_my_target_modal_visible(self) -> bool:
        return self.is_visible(SettingsCommonPageLocators.ADDIING_MY_TARGET_MODAL)

    def click_add_api_button(self):
        self.click(SettingsCommonPageLocators.ADD_API)

    def is_adding_api_modal_visible(self) -> bool:
        return self.is_visible(SettingsCommonPageLocators.ADDIING_API_MODAL)
