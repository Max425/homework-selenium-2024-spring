import time

from base_case import BaseCase
from ui.locators.money_page_locators import MoneyPageLocators


class TestMoneyPage(BaseCase):

    def test_content(self, money_page):
        assert money_page.find(MoneyPageLocators.TITLE).text == 'Зарабатывайте на вашем контенте'
        assert money_page.find(
            MoneyPageLocators.SUBTITLE).text == 'Вы вкладываете много сил в развитие вашего продукта — сайта или приложения. Рекламная сеть VK поможет вам получать от него прибыль.'

    def test_auth_btn(self, money_page):
        money_page.click(MoneyPageLocators.CABINET_BUTTON)
        money_page.go_to_new_tab()
        assert self.is_opened('https://id.vk.com/auth')

    def test_help_btn(self, money_page):
        money_page.click(MoneyPageLocators.HELP_BUTTON)
        money_page.go_to_new_tab()
        assert self.is_opened('https://ads.vk.com/help')

    def test_goods(self, money_page):
        assert money_page.page_contain_goods(money_page.GOODS)

    def test_formats(self, money_page):
        money_page.scroll_and_click(MoneyPageLocators.APP_BUTTON)
        assert money_page.page_contain_formats(money_page.APP_FORMATS)

        money_page.scroll_and_click(MoneyPageLocators.SITE_BUTTON)
        assert money_page.page_contain_formats(money_page.WEBSITE_FORMATS)

    def test_submit_button_disabled_if_form_not_valid(self, money_page):
        assert money_page.submit_button_is_disabled()
        money_page.enter_name_and_email('test', '')
        assert money_page.submit_button_is_disabled()


    def test_submit_button_enabled_after_filling_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        assert not money_page.submit_button_is_disabled()

    def test_submit_message_after_submitting_form(self, money_page):
        money_page.enter_name_and_email('test', 'test')
        money_page.scroll_and_click(MoneyPageLocators.SUBMIT_BUTTON)
        assert money_page.is_visible(MoneyPageLocators.SUBMIT_MESSAGE)
