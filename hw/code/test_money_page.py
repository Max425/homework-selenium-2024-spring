from base_case import BaseCase


class TestMoneyPage(BaseCase):

    def test_formats(self, money_page):
        money_page.app_btn_click()
        assert money_page.page_contain_formats(money_page.APP_FORMATS)

        money_page.site_btn_click()
        assert money_page.page_contain_formats(money_page.WEBSITE_FORMATS)

    def test_submit_button_disabled_if_form_not_valid_1(self, money_page):
        assert money_page.submit_button_is_disabled()
        money_page.enter_name_and_email('test', '')
        assert money_page.submit_button_is_disabled()

    def test_submit_button_disabled_if_form_not_valid_2(self, money_page):
        assert money_page.submit_button_is_disabled()
        money_page.enter_name_and_email('', 'test')
        assert money_page.submit_button_is_disabled()


    def test_submit_button_enabled_after_filling_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        assert not money_page.submit_button_is_disabled()

    def test_submit_message_after_submitting_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        money_page.submit_btn_click()
        assert money_page.is_submit_message_visible()
