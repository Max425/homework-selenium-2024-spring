import pytest

from base_case import BaseCase


class TestSettingsAccessPage(BaseCase):
    # def test_more_href(self, settings_access_page):
    #     settings_access_page.click_more_href()
    #     assert self.is_opened('https://ads.vk.com/help/articles/additionalaccounts')

    def test_add_cabinet_button(self, settings_access_page):
        settings_access_page.click_add_cabinet_button()
        assert settings_access_page.is_save_button_visible()

