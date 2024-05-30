from datetime import datetime
from base_case import BaseCase
import time

LEADFORM_NAME = 'Лид-форма ' + str(datetime.now().second)
COMPANY_NAME = 'Umlaut'
LEADFORM_TITLE = 'Заголовок 1'
LEADFORM_DESCRIPTION = 'Опрос 1'
COMPANY_LEGAL_NAME = 'OOO Umlaut'
COMPANY_ADRESS = 'Москва, улица Селениум, дом 3'

class TestLeadformPage(BaseCase):
    def test_create_leadform(self, leadform_page):
        leadform_page.click_create_leadform_button()
        assert leadform_page.is_leadform_page_opened()

        leadform_page.fill_leadform_name_field(LEADFORM_NAME)
        leadform_page.click_download_and_choose_logo_button()
        leadform_page.fill_company_name_field(COMPANY_NAME)
        leadform_page.fill_leadform_title_field(LEADFORM_TITLE)
        leadform_page.fill_leadform_description_field(LEADFORM_DESCRIPTION)
        leadform_page.click_save_button()

        assert leadform_page.is_question_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_result_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_settings_leadform_page_opened()
        leadform_page.fill_leadform_legal_name_field(COMPANY_LEGAL_NAME)
        leadform_page.fill_leadform_legal_adress_field(COMPANY_ADRESS)
        leadform_page.click_save_button()
        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

    def test_find_leadform(self, leadform_page):
        leadform_page.fill_find_leadform_field(LEADFORM_NAME)
        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

        unknown_leadform_name = 'Неизвестная лид-форма'
        leadform_page.fill_find_leadform_field(unknown_leadform_name)
        assert not leadform_page.is_leadform_in_list_exists(unknown_leadform_name)

    def test_cancel_create_leadform(self, leadform_page):
        leadform_page.click_create_leadform_button()
        assert leadform_page.is_leadform_page_opened()

        leadform_page.click_cancel_button()
        assert not leadform_page.is_leadform_page_opened()

    def test_delete_leadform(self, leadform_page):
        leadform_page.click_delete_leadform_button(LEADFORM_NAME)
        assert not leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

