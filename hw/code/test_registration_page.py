import time

from base_case import BaseCase


class TestRegistrationPage(BaseCase):
    def test_open_use_cabinet_myTarget(self, registration_page):
        registration_page.click_use_cabinet_myTarget_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/import/target')

    def test_open_new_cabinet_registration(self, registration_page):
        registration_page.click_create_new_cabinet_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/new')

    def test_change_account_type(self, registration_page, registration_new_page):
        registration_page.change_account_type('Рекламодатель')
        assert registration_page.is_physical_field_visible()

    def test_change_country(self, registration_page, registration_new_page):
        registration_page.change_country('Россия')
        assert registration_page.get_selected_currency('Российский рубль (RUB)') == 'Российский рубль (RUB)'

        registration_page.change_country('Беларусь')
        assert registration_page.get_selected_currency('Доллар США (USD)') == 'Доллар США (USD)'

    def test_required_email(self, registration_page, registration_new_page):
        registration_page.click_submit_button()
        assert registration_page.get_error() == 'Обязательное поле'

    def test_incorrect_email(self, registration_page, registration_new_page):
        registration_page.fill_email_field('aboba')
        registration_page.click_submit_button()
        assert registration_page.get_error() == 'Некорректный email адрес'

    def test_change_account_type_person(self, registration_page, registration_new_page):
        registration_page.change_account_type('Физическое лицо')
        assert registration_page.is_inn_field_visible()

        registration_page.change_account_type('Юридическое лицо')
        assert not registration_page.is_inn_field_visible()

    def test_incorrect_inn(self, registration_page, registration_new_page):
        registration_page.fill_email_field('xxx@xxx.ru')

        registration_page.fill_inn_field('123')
        registration_page.click_submit_button()
        assert registration_page.get_error() == 'Минимальная длина 12'

        registration_page.fill_inn_field('123123123123123')
        registration_page.click_submit_button()
        assert registration_page.get_error() == 'Максимальная длина 12 символов'

    def test_error_unaccepted_offer(self, registration_page, registration_new_page):
        registration_page.fill_email_field('xxx@xxx.ru')
        registration_page.fill_inn_field('123123123123')

        registration_page.click_offer_field()
        registration_page.click_submit_button()
        assert registration_page.get_error() == 'Обязательное поле'