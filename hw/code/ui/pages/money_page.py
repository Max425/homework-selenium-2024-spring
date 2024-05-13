from ui.pages.base_page import BasePage
from ui.locators.money_page_locators import MoneyPageLocators


class MoneyPage(BasePage):
    url = 'https://ads.vk.com/partner'

    GOODS = ['Стабильный спрос', 'Удобство пользователей', 'Подробная аналитика', 'Простое подключение']
    APP_FORMATS = ['Баннер', 'Нативный формат', 'Полноэкранный блок', 'Видео за вознаграждение']
    WEBSITE_FORMATS = ['Баннер', 'Instream', 'Адаптивный блок', 'InPage', 'Полноэкранный блок', 'Sticky-баннер']

    def page_contain_goods(self, item_names):
        for item_name in item_names:
            item = self.find(MoneyPageLocators.GOODS_ITEM_TITLE(item_name))
            if item is None:
                return False
        return True

    def page_contain_formats(self, item_names):
        for item_name in item_names:
            item = self.find(MoneyPageLocators.FORMAT_ITEM_TITLE(item_name))
            if item is None:
                return False
        return True

    def submit_button_is_disabled(self):
        return self.find(MoneyPageLocators.SUBMIT_BUTTON).get_attribute("disabled") is not None

    def enter_name_and_email(self, name, email):
        self.fill_field(MoneyPageLocators.NAME_INPUT, name)
        self.fill_field(MoneyPageLocators.EMAIL_INPUT, email)
