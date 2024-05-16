from ui.pages.base_page import BasePage
from ui.locators.settings_history_page_locators import SettingsHistoryPageLocators


class SettingsHistoryPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/logs'

    def click_filter_button(self):
        self.click(SettingsHistoryPageLocators.FILTER_BUTTON)

    def click_save_button(self):
        self.click(SettingsHistoryPageLocators.SAVE_BUTTON)

    def click_cancel_button(self):
        self.click(SettingsHistoryPageLocators.CANCEL_BUTTON)

    def select_filter_field(self, filter_name: str):
        self.click(SettingsHistoryPageLocators.SELECT_FILTER_FIELD(filter_name))

    def get_filter_field(self, filter_name: str):
        return self.find(SettingsHistoryPageLocators.CHECK_FILTER_FIELD(filter_name)).text

    def is_filter_field_visible(self, filter_name: str) -> bool:
        return self.is_visible(SettingsHistoryPageLocators.CHECK_FILTER_FIELD(filter_name))

    def is_save_button_visible(self) -> bool:
        return self.is_visible(SettingsHistoryPageLocators.SAVE_BUTTON)

    def click_filter_data_button(self):
        self.click(SettingsHistoryPageLocators.FILTER_DATA_BUTTON)

    def select_filter_data_field(self, filter_name: str):
        self.click(SettingsHistoryPageLocators.SELECT_FILTER_DATA_FIELD(filter_name))

    def click_cancel_data_button(self):
        self.click(SettingsHistoryPageLocators.CANCEL_DATA_BUTTON)
