from selenium.webdriver.support.wait import WebDriverWait

from base_case import BaseCase
from ui.fixtures import driver


class TestSettingsCommonPage(BaseCase):
    wait = WebDriverWait(driver, timeout=1)

    def test_save_button_visible(self, settings_common_page):
        assert not settings_common_page.is_save_button_visible()
        settings_common_page.enter_phone_number('1')
        assert settings_common_page.is_save_button_visible()

    def test_empty_phone_number(self, settings_common_page):
        settings_common_page.enter_name('q')
        settings_common_page.enter_phone_number('')
        self.wait.until(lambda d : settings_common_page.is_save_button_visible())
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Телефон не может быть короче 12 цифр'

    def test_short_phone_number(self, settings_common_page):
        settings_common_page.enter_phone_number('1')
        self.wait.until(lambda d : settings_common_page.is_save_button_visible())
        self.wait.until(lambda d : settings_common_page.is_save_button_enabled())
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректный номер телефона'

    def test_phone_number_without_plus(self, settings_common_page):
        settings_common_page.enter_phone_number('89099883947')
        self.wait.until(lambda d : settings_common_page.is_save_button_visible())
        self.wait.until(lambda d : settings_common_page.is_save_button_enabled())
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректный номер телефона'
    
    def test_empty_inn(self, settings_common_page):
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_name('q')
        settings_common_page.enter_inn('')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректные символы. Разрешена только кириллица дефис и пробел'

    def test_short_inn(self, settings_common_page): 
        settings_common_page.enter_name('q')
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Длина ИНН должна быть 12 символов'

    def test_incorrect_inn(self, settings_common_page):
        settings_common_page.enter_name('q')
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123123123123')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Невалидный ИНН'

    def test_add_email_input_is_visible(self, settings_common_page):
        assert not settings_common_page.is_email_input_visible()
        settings_common_page.click_add_email_button()
        assert settings_common_page.is_email_input_visible()
    
    def test_add_empty_email(self, settings_common_page):
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123123123123')
        settings_common_page.enter_name('q')
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Обязательное поле'
    
    def test_add_incorrect_email_without_dog(self, settings_common_page):
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123123123123')
        settings_common_page.enter_name('q')
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('qwertymail.ru')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректный email адрес'
    
    def test_add_incorrect_email_without_dot(self, settings_common_page):
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123123123123')
        settings_common_page.enter_name('q')
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('qwerty@mailru')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректный email адрес'
    
    def test_add_incorrect_email_with_kirillitsa(self, settings_common_page):
        settings_common_page.enter_phone_number('+79099883947')
        settings_common_page.enter_inn('123123123123')
        settings_common_page.enter_name('q')
        settings_common_page.click_add_email_button()
        settings_common_page.enter_email('абвг@mail.ru')
        settings_common_page.click_save_button()
        assert settings_common_page.get_error_text() == 'Некорректный email адрес'

    def test_add_email_input_is_closed(self, settings_common_page):
        settings_common_page.click_add_email_button()
        assert settings_common_page.is_email_input_visible()
        settings_common_page.click_close_email_button()
        assert not settings_common_page.is_email_input_visible()

    def test_add_my_target(self, settings_common_page):
        settings_common_page.click_add_my_target_button()
        assert settings_common_page.is_adding_my_target_modal_visible()

    def test_add_api(self, settings_common_page):
        settings_common_page.click_add_api_button()
        assert settings_common_page.is_adding_api_modal_visible()
