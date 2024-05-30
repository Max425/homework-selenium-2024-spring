from ui.pages.base_page import BasePage
from ui.locators.settings_notifications_page_locators import SettingsNotificationsPageLocators


class SettingsNotificationsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/notifications'

    def click_email_checkbox(self):
        self.click(SettingsNotificationsPageLocators.EMAIL_CHECKBOX)

    def click_save_button(self):
        self.click(SettingsNotificationsPageLocators.SAVE_BUTTON)

    def is_save_button_visible(self) -> bool:
        return self.is_visible(SettingsNotificationsPageLocators.SAVE_BUTTON)

    def is_save_button_not_visible(self) -> bool:
        return not self.is_visible(SettingsNotificationsPageLocators.SAVE_BUTTON)

    def is_save_button_enabled(self) -> bool:
        return self.find(SettingsNotificationsPageLocators.SAVE_BUTTON).is_enabled()

    def click_cancel_button(self):
        self.click(SettingsNotificationsPageLocators.CANCEL_BUTTON)

    def click_notification_setting_field(self, select_type: str):
        self.click(SettingsNotificationsPageLocators.SELECT_NOTIFICATION_SETTING(select_type))
