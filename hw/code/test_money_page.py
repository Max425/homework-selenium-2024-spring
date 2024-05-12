from base_case import BaseCase
from ui.locators.money_page_locators import MoneyPageLocators


class TestMoneyPage(BaseCase):
    def test_go_to_auth(self, money_page):
        money_page.click(MoneyPageLocators.CABINET_BUTTON)
        money_page.go_to_new_tab()
        assert self.is_opened('https://id.vk.com/auth')

    def test_go_to_help(self, money_page):
        money_page.click(MoneyPageLocators.HELP_BUTTON)
        money_page.go_to_new_tab()
        assert self.is_opened('https://ads.vk.com/help')

    def test_formats(self, money_page):
        money_page.click_format_tab('Для приложений')
        assert money_page.page_contain_formats(money_page.APP_FORMATS)

        money_page.click_format_tab('Для сайтов')
        assert money_page.page_contain_formats(money_page.WEBSITE_FORMATS)

    def test_submit_button_disabled_by_default(self, money_page):
        assert money_page.submit_button_is_disabled()

    def test_submit_button_enabled_after_filling_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        assert not money_page.submit_button_is_disabled()

    def test_submit_message_after_submitting_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        money_page.click_submit_button()
        assert money_page.submit_message_became_visible()