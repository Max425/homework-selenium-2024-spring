from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from ui.locators.audience_page_locators import AudiencePageLocators
from ui.pages.base_page import BasePage
from selenium.common import TimeoutException


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def is_create_audience_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Создание аудитории"))

    def is_create_audience_modal_invisible(self) -> bool:
        return not self.is_visible(self.locators.MODAL("Создание аудитории"))

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

    def is_add_source_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Включить источник"))

    def is_add_source_modal_invisible(self) -> bool:
        return not self.is_visible(self.locators.MODAL("Включить источник"))

    def is_vk_group_subscribers_modal_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL("Подписчики сообществ"))

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

    def get_period_input_value(self) -> WebElement:
        return self.find(self.locators.MODAL_INPUT("Период поиска")).get_attribute('value')
    
    def fill_period_input(self, value):
        period_input = self.find(self.locators.MODAL_INPUT("Период поиска"))
        period_input.send_keys(Keys.CONTROL,"a")
        period_input.send_keys(Keys.BACKSPACE)
        period_input.send_keys(value)

    def get_period_input_value(self) -> WebElement:
        return self.find(self.locators.MODAL_INPUT("Период поиска")).get_attribute('value')

    def enter_period(self, period) -> WebElement:
        input = self.find(self.locators.MODAL_INPUT("Период поиска"))
        input.clear()
        input.send_keys(period)

    def get_period_input_value(self) -> WebElement:
        return self.find(self.locators.MODAL_INPUT("Период поиска")).get_attribute('value')

    def enter_period(self, period) -> WebElement:
        input = self.find(self.locators.MODAL_INPUT("Период поиска"))
        input.clear()
        input.send_keys(period)

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text

    def is_add_source_button_visible(self) -> bool:
        return self.is_visible(self.locators.ADD_SOURCE_BUTTON)

    def is_source_select_button_visible(self, label) -> bool:
        return self.is_visible(self.locators.SOURCE_ITEM(label))

    def is_modal_field_visible(self, label):
        return self.is_visible(self.locators.MODAL_FIELD(label)) or self.is_visible(self.locators.MODAL_INPUT(label))

    def is_submit_button_enabled(self) -> bool:
        submit_button = self.find(self.locators.MODAL_SUBMIT_BUTTON)
        return submit_button.is_enabled()

    def click_submit_button(self) -> bool:
        self.click(self.locators.MODAL_SUBMIT_BUTTON)

    def get_error_text(self) -> str:
        return self.find(self.locators.ERROR).text
    
    def get_created_audience(self, name):
        return self.find(self.locators.AUDIENCE_CREATED(name))
    
    def is_created_audience_visible(self, name):
        return self.is_visible(self.locators.AUDIENCE_CREATED(name))
    
    def delete_audience(self):
        self.click(self.locators.AUDIENCE_SELECT)
        self.click(self.locators.AUDIENCE_DELETE)
        self.click(self.locators.AUDIENCE_APROVE_DELETING)

    def create_audience(self):
        self.click(self.locators.AUDIENCE_CREATE)

    def enter_vk_group_link(self, group_link: str):
        elem = self.find(self.locators.GROUP_LINK_INPUT)
        elem.clear()
        elem.send_keys(group_link)

    def select_vk_group(self):
        self.click(self.locators.GROUP_SELECT)
        self.click(self.locators.GROUP_OPTION)
        self.click(self.locators.MODAL("Подписчики сообществ"))

    def create_audience_by_subscribers(self):
        self.click(self.locators.AUDIENCE_CREATE_SUBSCRIBERS)

    def check_selected_group(self):
        return self.find(self.locators.SELECTED_GROUP).text

    def add_many_vk_group(self):
        self.click(self.locators.ADD_MANY_GROUPS_BTN)
        self.click(self.locators.SELECT_VK_GROUPS)
    
    def is_modal_add_vk_groups_visible(self):
        return self.is_visible(self.locators.SELECT_MANY_GROUPS_MODAL)

    def add_groups(self, group_link):
        elem = self.find(self.locators.MODAL_FIELD(''))
        elem.clear()
        elem.send_keys(group_link)

    def get_adding_groups_status(self):
        return self.find(self.locators.ADD_MANY_GROUPS_SUCCESS).text

    def add_groups_to_auditory(self):
        self.click(self.locators.COMPLETE_ADD_MANY_GROUPS_BTN)
    
    def close_modal(self):
        self.click(self.locators.CLOSE_BTN)
