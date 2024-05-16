from ui.locators.ecomm_page_locators import EcommPageLocators
from ui.pages.base_page import BasePage


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def cancel_education(self):
        self.click(self.locators.CANCEL_EDUCATION)

    def is_education_modal_closed(self):
        return not self.is_visible(self.locators.MODAL_EDUCATION)

    def create_new_catalog(self):
        self.click(self.locators.CREATE_CATALOG_COMMON_BUTTON)

    def close(self):
        self.click(self.locators.CROSS)

    def is_new_catalog_modal_page_became_visible(self) -> bool:
        return self.is_visible(self.locators.MODAL_OF_NEW_CATALOG, 10)

    def is_new_catalog_modal_page_became_invisible(self) -> bool:
        return not self.is_visible(self.locators.MODAL_OF_NEW_CATALOG)

    def enter_catalog_name(self, name: str):
        amount_input = self.find(self.locators.CATALOG_NAME_INPUT)
        amount_input.clear()
        amount_input.send_keys(name)

    def get_error_text(self) -> str:
        return self.find(self.locators.ERROR_MESSAGE).text

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
        self.click(self.locators.GOOD_DROPDOWN)

    def choose_good_category(self):
        self.click(self.locators.GOOD_AUTO)

    def get_choosed_good_category(self):
        return self.find(self.locators.GOOD_EXAMPLE).text

    def catalog_table_is_created(self) -> bool:
        return self.is_visible(self.locators.CATALOGS_TABLE)
