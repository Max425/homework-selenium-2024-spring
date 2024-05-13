from ui.pages.base_page import BasePage
from ui.locators.ecomm_page_locators import EcommPageLocators


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def create_new_catalog(self):
        self.click(self.locators.CREATE_CATALOG_COMMON_BUTTON)

    def new_catalog_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.MODAL_OF_NEW_CATALOG)
    
    def enter_catalog_name(self, name: str):
        amount_input = self.find(self.locators.CATALOG_NAME_INPUT)
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

    def enter_feed_url(self, url: str):
        amount_input = self.find(self.locators.FEED_URL_INPUT)
        amount_input.clear()
        amount_input.send_keys(url)
