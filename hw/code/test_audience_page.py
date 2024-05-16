import pytest
import time
from base_case import BaseCase

KEY_PHRASES_SOURCE = 'Ключевые фразы'
KEY_PHRASE = "люблю вк"


@pytest.fixture
def create_audience_modal_page(audience_page):
    audience_page.click_create_audience_button()


@pytest.fixture
def key_phrases_source(create_audience_modal_page, audience_page):
    audience_page.click_add_source_button()
    audience_page.select_source(KEY_PHRASES_SOURCE)


class TestAudiencePage(BaseCase):  
    def test_create_audience_modal_opens(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.create_audience_modal_visible()
        assert audience_page.is_add_source_button_visible()

    def test_add_source_modal_opens(self, create_audience_modal_page, audience_page):
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_visible()
        for source in ["Существующая аудитория", "Список пользователей", "Ключевые фразы", "События в рекламной кампании"]:
            assert audience_page.is_source_select_button_visible(source)

    def test_key_pharases_opens(self, create_audience_modal_page, audience_page):
        audience_page.click_add_source_button()
        audience_page.select_source(KEY_PHRASES_SOURCE)
        for field in ["Название", "Ключевые фразы", "Минус-фразы", "Период поиска"]:
            assert audience_page.is_modal_field_visible(field)

    def test_add_source_by_key_phrases(self, key_phrases_source, audience_page):
        assert not audience_page.is_submit_button_enabled()
        audience_page.enter_key_phrases(KEY_PHRASE)
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        assert KEY_PHRASE in audience_page.get_source_card_content()

    def test_add_source_by_key_phrases_not_full_form(self, key_phrases_source, audience_page):
        audience_page.enter_minus_phrases('минус')
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        assert "Обязательное поле" == audience_page.get_error_text()

    def test_add_source_by_key_phrases_incorrect_period(self, key_phrases_source, audience_page):
        audience_page.fill_period_input('0')
        time.sleep(1)   # sleep это часть теста
        assert audience_page.get_period_input_value() == "1"
