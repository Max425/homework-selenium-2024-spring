import pytest
from datetime import datetime
from base_case import BaseCase
import time

KEY_PHRASES_SOURCE = 'Ключевые фразы'
DEFAULT_AUDIENCE_NAME = 'Аудитория ' + datetime.now().strftime('%Y-%m-%d')
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
        assert audience_page.get_default_audience_name() == DEFAULT_AUDIENCE_NAME
        assert audience_page.is_visible(audience_page.locators.ADD_SOURCE_BUTTON) 
        
    def test_add_source_modal_opens(self, create_audience_modal_page, audience_page):
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_visible()
        for source in ["Существующая аудитория", "Список пользователей", "Ключевые фразы", "События в рекламной кампании"]:
            assert audience_page.is_visible(audience_page.locators.SOURCE_ITEM(source))

    def test_key_pharases_opens(self, create_audience_modal_page, audience_page):
        audience_page.click_add_source_button()
        audience_page.select_source(KEY_PHRASES_SOURCE)
        modal = audience_page.get_key_phrases_modal()
        for field in ["Название", "Ключевые фразы", "Минус фразы", "Период поиска"]:
            assert field in modal.get_attribute("innerHTML")

    def test_add_source_by_key_phrases(self, key_phrases_source, audience_page):
        submit_button = audience_page.find(audience_page.locators.MODAL_SUBMIT_BUTTON)
        assert not submit_button.is_enabled()
        audience_page.enter_key_phrases(KEY_PHRASE)
        assert submit_button.is_enabled()
        submit_button.click()
        assert KEY_PHRASE in audience_page.get_source_card_content()

    def test_add_source_by_key_phrases_not_full_form(self, key_phrases_source, audience_page):
        submit_button = audience_page.find(audience_page.locators.MODAL_SUBMIT_BUTTON)
        audience_page.enter_minus_phrases('минус')
        assert submit_button.is_enabled()
        submit_button.click()
        assert "Обязательное поле" == audience_page.find(audience_page.locators.ERROR).text

    def test_add_source_by_key_phrases_incorrect_period(self, key_phrases_source, audience_page):
        period_input = audience_page.get_period_input()
        period_input.clear()
        time.sleep(1)
        assert period_input.get_attribute('value') == "1"