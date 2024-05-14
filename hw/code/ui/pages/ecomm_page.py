from ui.pages.base_page import BasePage
from ui.locators.ecomm_page_locators import EcommPageLocators
from selenium.webdriver.support.ui import Select


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def cancel_education(self):
        self.click(self.locators.CANCEL_EDUCATION)

    def create_new_catalog(self):
        self.click(self.locators.CREATE_CATALOG_COMMON_BUTTON)

    def close(self):
        self.click(self.locators.CROSS)

    def new_catalog_modal_page_became_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL_OF_NEW_CATALOG, 10)
    
    def new_catalog_modal_page_became_invisible(self) -> bool:
        return self.is_visible(self.locators.MODAL_OF_NEW_CATALOG)
    
    def enter_catalog_name(self, name: str):
        amount_input = self.find(self.locators.PHONE_INPUT)
        amount_input.clear()
        amount_input.send_keys(name)

    def get_catalog_page_title(self) -> str:
        return self.find(self.locators.CATALOG_NAME_HEADER).text
    
    def get_catalog_name_title(self) -> str:
        return self.find(self.locators.CREATE_CATALOG_HEADER).text
    
    def get_adding_positions_title(self) -> str:
        return self.find(self.locators.ADDING_POSITIONS_HEADER).text
    
    def get_position_feed_or_comunity_title(self) -> str:
        return self.find(self.locators.FEED_OR_COMUNITY_HEADER).text
    
    def get_position_marketplace_title(self) -> str:
        return self.find(self.locators.MARKETPLACE_HEADER).text
    
    def get_position_file_title(self) -> str:
        return self.find(self.locators.ADD_FILE_HEADER).text
    
    def get_error_text(self) -> str:
        return self.find(self.locators.ERROR_MESSAGE).text
    
    def get_error_modal_text(self) -> str:
        return self.find(self.locators.MODAL_OF_ERROR).text

    def add_position_feed_or_comunity(self):
        self.click(self.locators.FEED_OR_COMUNITY)

    def add_position_marketplace(self):
        self.click(self.locators.MARKETPLACE)
    
    def add_position_add_file(self):
        self.click(self.locators.ADD_FILE)

    def finish_creating_catalog(self):
        self.click(self.locators.CREATE_CATALOG_FINISH_BUTTON)

    def cancel_creating_catalog(self):
        self.click(self.locators.CANCEL_CATALOG_FINISH_BUTTON)

    def enter_url(self, url: str):
        amount_input = self.find(self.locators.URL_INPUT)
        amount_input.clear()
        amount_input.send_keys(url)

    def get_api_key_field(self):
        return self.find(self.locators.ADD_API_KEY).text
    
    def change_good_category(self):
        sel = Select(self.locators.GOOD_DROPDOWN)
        sel.select_by_value('auto')

    def choose_good_category(self):
        self.click(self.locators.GOOD_AUTO)

    def get_choosed_good_category(self):
        return self.find(self.locators.GOOD_EXAMPLE).text
