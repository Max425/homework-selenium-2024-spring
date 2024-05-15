from base_case import BaseCase


class TestSettingsNotificationsPage(BaseCase):
    def test_save_button_visible(self, settings_notifications_page):
        assert not settings_notifications_page.is_save_button_visible()
        settings_notifications_page.click_email_checkbox()
        assert settings_notifications_page.is_save_button_visible()
        assert not settings_notifications_page.is_save_button_enabled()

    def test_cancel_button(self, settings_notifications_page):
        settings_notifications_page.click_email_checkbox()
        settings_notifications_page.click_notification_setting_field('Модерация')
        settings_notifications_page.click_cancel_button()
        assert not settings_notifications_page.is_save_button_visible()

    def test_save_setting(self, settings_notifications_page):
        settings_notifications_page.click_email_checkbox()
        settings_notifications_page.click_notification_setting_field('Модерация')
        assert settings_notifications_page.is_save_button_enabled()

        settings_notifications_page.click_save_button()
        assert not settings_notifications_page.is_save_button_visible()
        settings_notifications_page.click_email_checkbox()
        assert settings_notifications_page.is_save_button_enabled()
        settings_notifications_page.click_save_button()
