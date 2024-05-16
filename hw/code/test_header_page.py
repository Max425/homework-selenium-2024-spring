from base_case import BaseCase


class TestHeaderPage(BaseCase):
    def test_open_training_button(self, header_page):
        header_page.click_vk_logo_button()
        assert self.is_opened('https://ads.vk.com/hq/overview')

    def test_change_accounts_button(self, header_page):
        header_page.click_change_account_button()
        header_page.click_all_cabinets_button()
        assert self.is_opened('https://ads.vk.com/hq/settings/access')

    def test_notifications_button(self, header_page):
        header_page.click_notifications_button()
        assert header_page.is_modal_notifications_visible()

    def test_user_avatar_button(self, header_page):
        header_page.click_user_avatar_button()
        header_page.click_quit_button()
        assert self.is_opened('https://ads.vk.com/')