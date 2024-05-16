from selenium.webdriver.support.wait import WebDriverWait

from base_case import BaseCase
from ui.fixtures import driver


class TestEcommPage(BaseCase):
    wait = WebDriverWait(driver, timeout=1)

    def test_open_modal(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        assert ecomm_page.is_new_catalog_modal_page_became_visible()

    def test_empty_feed_url(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Обязательное поле'
        
    def test_incorrect_feed_url_h(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('h')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_feed_url_http(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_feed_url_invalid_url(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http://')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Невалидный url'

    def test_incorrect_feed_url_invalid_url_send(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http://a')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Неверный статус HTTP-запроса'

    def test_empty_marketplace_url(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Обязательное поле'
        
    def test_incorrect_marketplace_url_h(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('h')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_marketplace_url_http(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_marketplace_url_invalid_url(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http://')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Невалидный url'

    def test_incorrect_marketplace_url_invalid_url_send(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http://a')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе'

    def test_correct_marketplace_url(self, ecomm_page):
        ecomm_page.cancel_education()
        self.wait.until(lambda d : ecomm_page.is_education_modal_closed())
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('https://www.wildberries.ru/brands/975102-health-body')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_api_key_field() == 'API key'
