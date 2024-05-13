from base_case import BaseCase


class TestRegistrationPage(BaseCase):
    def test_open_campaings(self, menu_page):
        menu_page.click_campaings_button()
        assert self.is_opened('https://ads.vk.com/hq/dashboard/ad_plans')

    def test_open_audience(self, menu_page):
        menu_page.click_audience_button()
        assert self.is_opened('https://ads.vk.com/hq/audience')

    def test_open_budget(self, menu_page):
        menu_page.click_budget_button()
        assert self.is_opened('https://ads.vk.com/hq/budget/transactions')

    def test_open_ecomm_catalogs(self, menu_page):
        menu_page.click_ecomm_catalogs_button()
        assert self.is_opened('https://ads.vk.com/hq/ecomm/catalogs')

    def test_open_pixels_button(self, menu_page):
        menu_page.click_pixels_button()
        assert self.is_opened('https://ads.vk.com/hq/pixels')

    def test_open_apps_button(self, menu_page):
        menu_page.click_apps_button()
        assert self.is_opened('https://ads.vk.com/hq/apps')

    def test_open_leadads_button(self, menu_page):
        menu_page.click_leadads_button()
        assert self.is_opened('https://ads.vk.com/hq/leadads/leadforms')

    def test_open_training_button(self, menu_page):
        menu_page.click_training_button()
        assert menu_page.is_modal_training_visible()

    def test_open_settings_button(self, menu_page):
        menu_page.click_settings_button()
        assert self.is_opened('https://ads.vk.com/hq/settings')