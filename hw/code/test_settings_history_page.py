from base_case import BaseCase


class TestSettingsHistoryPage(BaseCase):

    def test_filter_button(self, settings_history_page):
        settings_history_page.click_filter_button()
        assert settings_history_page.is_save_button_visible()

    def test_cancel_filter(self, settings_history_page):
        settings_history_page.click_filter_button()
        assert settings_history_page.is_save_button_visible()
        settings_history_page.select_filter_field('Кампания')
        settings_history_page.click_cancel_button()
        assert not settings_history_page.is_filter_field_visible('Кампания')

    def test_save_filter(self, settings_history_page):
        settings_history_page.click_filter_button()
        assert settings_history_page.is_save_button_visible()
        settings_history_page.select_filter_field('Кампания')
        settings_history_page.click_save_button()
        assert settings_history_page.is_filter_field_visible('Кампания')
        assert settings_history_page.get_filter_field('Кампания') == 'Кампания'

    def test_filter_data_button(self, settings_history_page):
        settings_history_page.click_filter_data_button()
        assert settings_history_page.is_save_button_visible()

    def test_cancel_filter_data(self, settings_history_page):
        settings_history_page.click_filter_data_button()
        assert settings_history_page.is_save_button_visible()
        settings_history_page.select_filter_data_field('Последний 31 день')
        settings_history_page.click_cancel_data_button()
        assert not settings_history_page.is_filter_field_visible('Последний 31 день')