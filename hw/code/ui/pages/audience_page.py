from selenium.common import TimeoutException
from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from ui.locators.audience_page_locators import AudiencePageLocators
from datetime import datetime


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def create_audience_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Создание аудитории"))

    def get_default_audience_name(self):
        return self.find(self.locators.AUDIENCE_NAME_INPUT).get_attribute('value')

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON)

    def add_source_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Включить источник"))

    def get_add_source_modal(self) -> WebElement:
        return self.find(self.locators.MODAL("Включить источник"))

    def key_phrases_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Ключевые фразы"))

    def get_key_phrases_modal(self) -> WebElement:
        return self.find(self.locators.MODAL("Ключевые фразы"))

    def select_source(self, source_name):
        self.click(self.locators.SOURCE_ITEM(source_name))

    def enter_key_phrases(self, key_phrases: str):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(key_phrases)

    def click_modal_page_submit_button(self):
        self.click(self.locators.MODAL_SUBMIT_BUTTON)

    def enter_minus_phrases(self, phrases):
        minus_phrases_input = self.find(self.locators.MODAL_FIELD("Минус-фразы"))
        minus_phrases_input.clear()
        minus_phrases_input.send_keys(phrases)

    def get_period_input(self) -> WebElement:
        return self.find(self.locators.MODAL_INPUT("Период поиска"))

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text