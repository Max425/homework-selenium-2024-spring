from ui.pages.base_page import BasePage
from ui.locators.money_page_locators import MoneyPageLocators


class MoneyPage(BasePage):
    url = 'https://ads.vk.com/partner'

    GOODS = ['Стабильный спрос', 'Удобство пользователей', 'Подробная аналитика', 'Простое подключение']
    APP_FORMATS = ['Баннер', 'Нативный формат', 'Полноэкранный блок', 'Видео за вознаграждение']
    WEBSITE_FORMATS = ['Баннер', 'Instream', 'Адаптивный блок', 'InPage', 'Полноэкранный блок', 'Sticky-баннер']

    def page_contain_goods(self, item_names):
        return all(self.find(MoneyPageLocators.GOODS_ITEM_TITLE(item_name)) for item_name in item_names)

    def page_contain_formats(self, item_names):
        return all(self.find(MoneyPageLocators.FORMAT_ITEM_TITLE(item_name)) for item_name in item_names)

    def submit_button_is_disabled(self):
        return self.find(MoneyPageLocators.SUBMIT_BUTTON).get_attribute("disabled") is not None

    def enter_name_and_email(self, name, email):
        self.fill_field(MoneyPageLocators.NAME_INPUT, name)
        self.fill_field(MoneyPageLocators.EMAIL_INPUT, email)

    def title_text(self):
        return self.find(MoneyPageLocators.TITLE).text

    def subtitle_text(self):
        return self.find(MoneyPageLocators.SUBTITLE).text

    def cabinet_btn_click(self):
        return self.click(MoneyPageLocators.CABINET_BUTTON)

    def help_btn_click(self):
        return self.click(MoneyPageLocators.HELP_BUTTON)

    def app_btn_click(self):
        return self.scroll_and_click(MoneyPageLocators.APP_BUTTON)

    def site_btn_click(self):
        return self.scroll_and_click(MoneyPageLocators.SITE_BUTTON)

    def submit_btn_click(self):
        return self.scroll_and_click(MoneyPageLocators.SUBMIT_BUTTON)

    def is_submit_message_visible(self):
        return self.is_visible(MoneyPageLocators.SUBMIT_MESSAGE)
