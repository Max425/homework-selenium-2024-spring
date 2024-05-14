import time

from base_case import BaseCase


class TestEcommPage(BaseCase):

    def test_open_modal(self, ecomm_page):
        ecomm_page.cancel_education()
        time.sleep(1)
        ecomm_page.create_new_catalog()
        assert ecomm_page.new_catalog_modal_page_became_visible()

    def test_empty_catalog_name(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.enter_catalog_name('')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Обязательное поле'

    def test_empty_feed_url(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Обязательное поле'

    def test_incorrect_feed_url_h(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('h')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_feed_url_http(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_feed_url_invalid_url(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http://')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Невалидный url'

    def test_incorrect_feed_url_invalid_url_send(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('http://a')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Неверный статус HTTP-запроса'

    def test_incorrect_feed_url_valid_url_send(self, ecomm_page):
        ecomm_page.cancel_education()
        time.sleep(1)
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_feed_or_comunity()
        ecomm_page.enter_url('https://vk.com/ksnlkkslnk')
        time.sleep(1)
        ecomm_page.finish_creating_catalog()
        time.sleep(5)
        assert ecomm_page.new_catalog_modal_page_became_invisible() == False

    def test_empty_marketplace_url(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.close()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Обязательное поле'

    def test_incorrect_marketplace_url_h(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('h')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_marketplace_url_http(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Необходимо указать протокол http(s)'

    def test_incorrect_marketplace_url_invalid_url(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http://')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Невалидный url'

    def test_incorrect_marketplace_url_invalid_url_send(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('http://a')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_text() == 'Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе'

    def test_correct_marketplace_url(self, ecomm_page):
        ecomm_page.cancel_education()
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_marketplace()
        ecomm_page.enter_url('https://www.wildberries.ru/brands/975102-health-body')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_api_key_field() == 'API key'

    def test_change_good_type(self, ecomm_page):
        ecomm_page.cancel_education()
        time.sleep(1)
        ecomm_page.create_new_catalog()
        ecomm_page.add_position_add_file()
        ecomm_page.change_good_category()
        assert ecomm_page.get_choosed_good_category() == 'Скачать шаблон фида "Авто"'
