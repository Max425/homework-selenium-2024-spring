from datetime import datetime
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from ui.fixtures import driver

from base_case import BaseCase

KEY_PHRASES_SOURCE = 'Ключевые фразы'
KEY_PHRASE = "люблю вк"


@pytest.fixture
def create_audience_modal_page(audience_page):
    audience_page.click_create_audience_button()


@pytest.fixture
def key_phrases_source(create_audience_modal_page, audience_page):
    audience_page.click_add_source_button()
    audience_page.select_source('Ключевые фразы')


class TestAudiencePage(BaseCase): 
    wait = WebDriverWait(driver, timeout=0)

    def test_add_source_by_key_phrases(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.is_create_audience_modal_visible()
        assert audience_page.get_default_audience_name() == "Аудитория " + datetime.now().strftime("%Y-%m-%d")
        assert audience_page.is_add_source_button_visible()
        audience_page.click_add_source_button()
        assert audience_page.is_add_source_modal_visible()
        for source in ["Существующая аудитория", "Список пользователей", "Ключевые фразы",
                       "События в рекламной кампании"]:
            assert audience_page.is_source_select_button_visible(source)
        audience_page.select_source('Ключевые фразы')
        for field in ["Название", "Ключевые фразы", "Минус-фразы", "Период поиска"]:
            assert audience_page.is_modal_field_visible(field)
        assert not audience_page.is_submit_button_enabled()
        audience_page.enter_key_phrases("люблю вк")
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        assert "люблю вк" in audience_page.get_source_card_content()
        audience_page.create_audience()
        assert ("Аудитория " + datetime.now().strftime("%Y-%m-%d")) in audience_page.get_created_audience()
        audience_page.delete_audience()

    def test_add_source_by_key_and_minus_phrases(self, key_phrases_source, audience_page):
        audience_page.enter_minus_phrases('минус')
        assert not audience_page.is_submit_button_enabled()
        audience_page.enter_key_phrases("люблю вк")
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        assert "люблю вк" in audience_page.get_source_card_content()
        audience_page.create_audience()
        assert ("Аудитория " + datetime.now().strftime("%Y-%m-%d")) in audience_page.get_created_audience()
        audience_page.delete_audience()

    def test_add_source_by_existing_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(KEY_PHRASES_SOURCE)
        assert not audience_page.is_submit_button_enabled()
        audience_page.enter_key_phrases(KEY_PHRASE)
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        self.wait.until(lambda d : audience_page.is_add_source_modal_invisible())
        audience_page.create_audience()
        self.wait.until(lambda d : audience_page.is_create_audience_modal_invisible())
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source("Существующая аудитория")
        audience_page.delete_audience()

    def test_add_source_by_vk_group(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.is_create_audience_modal_visible()
        audience_page.click_add_source_button()
        assert audience_page.is_add_source_modal_visible()
        audience_page.select_source('Подписчики сообществ')
        assert audience_page.is_vk_group_subscribers_modal_visible()
        audience_page.enter_vk_group_link('https://vk.com/art.jpgg')
        audience_page.select_vk_group()
        assert 'A!' == audience_page.check_selected_group()
        audience_page.create_audience_by_subscribers()
        self.wait.until(lambda d : audience_page.is_add_source_modal_invisible())
        audience_page.create_audience()
        assert audience_page.get_created_audience("Аудитория " + datetime.now().strftime("%Y-%m-%d"))
        audience_page.delete_audience()

    def test_add_source_by_some_of_vk_group(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.is_create_audience_modal_visible()
        audience_page.click_add_source_button()
        assert audience_page.is_add_source_modal_visible()
        audience_page.select_source('Подписчики сообществ')
        assert audience_page.is_vk_group_subscribers_modal_visible()
        audience_page.add_many_vk_group()
        assert audience_page.is_modal_add_vk_groups_visible()
        audience_page.add_groups('https://vk.com/art.jpgg\nhttps://vk.com/mrtdll')
        audience_page.add_groups_to_auditory()
        assert 'Добавлено 2 сообщества' == audience_page.get_adding_groups_status()
        audience_page.close_modal()
        assert 'A!' == audience_page.check_selected_group()
        audience_page.create_audience_by_subscribers()
        self.wait.until(lambda d : audience_page.is_add_source_modal_invisible())
        audience_page.create_audience()
        assert audience_page.get_created_audience("Аудитория " + datetime.now().strftime("%Y-%m-%d"))
        audience_page.delete_audience()

    def test_deleting(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(KEY_PHRASES_SOURCE)
        audience_page.enter_key_phrases(KEY_PHRASE)
        audience_page.click_submit_button()
        audience_page.create_audience()
        assert audience_page.get_created_audience("Аудитория " + datetime.now().strftime("%Y-%m-%d"))
        audience_page.delete_audience()
        assert not audience_page.is_created_audience_visible("Аудитория " + datetime.now().strftime("%Y-%m-%d"))

    def test_add_zero_search_period(self, key_phrases_source, audience_page):
        audience_page.enter_period('0')
        audience_page.enter_minus_phrases('')
        assert audience_page.get_period_input_value() == '1'

    def test_edit_auditory(self, audience_page):
        audience_page.click_auditory("Аудитория " + datetime.now().strftime("%Y-%m-%d"))
        audience_page.click_edit()
        for field in ["Название", "Ключевые фразы", "Минус-фразы", "Период поиска"]:
            assert audience_page.is_modal_field_visible(field)
        audience_page.enter_key_phrases("люблю вк")
        assert audience_page.is_submit_button_enabled()
        audience_page.click_submit_button()
        assert "люблю вк" in audience_page.get_source_card_content()
        audience_page.create_audience()
        assert ("Аудитория " + datetime.now().strftime("%Y-%m-%d")) in audience_page.get_created_audience()
        audience_page.delete_audience()
        audience_page.click_auditory("Аудитория " + datetime.now().strftime("%Y-%m-%d"))
        assert "люблю вк" in audience_page.get_source_card_content()
        
        
        


    
        