from ui.locators.ecomm_page_locators import EcommPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def cancel_education(self):
        if self.is_visible(self.locators.CANCEL_EDUCATION, timeout=3):
            self.click(self.locators.CANCEL_EDUCATION)
            self.click(self.locators.CLOSE_EDUCATION_BUTTON)

    def is_education_modal_closed(self):
        return self.is_invisible(self.locators.MODAL_EDUCATION)

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
    
    def get_error_banner_text(self) -> str:
        return self.find(self.locators.ERROR_MESSAGE_BANNER).text

    def add_position_feed_or_comunity(self):
        self.click(self.locators.FEED_OR_COMUNITY)

    def add_position_marketplace(self):
        self.click(self.locators.MARKETPLACE)

    def add_position_add_file(self):
        self.click(self.locators.ADD_FILE)

    def finish_creating_catalog(self):
        self.wait().until(EC.element_to_be_clickable(self.locators.CREATE_CATALOG_FINISH_BUTTON))
        button = self.find(self.locators.CREATE_CATALOG_FINISH_BUTTON)
        time.sleep(1)
        button.click()
        #self.click(self.locators.CREATE_CATALOG_FINISH_BUTTON)

    def cancel_creating_catalog(self):
        self.wait().until(EC.element_to_be_clickable(self.locators.CANCEL_CATALOG_FINISH_BUTTON))
        self.click(self.locators.CANCEL_CATALOG_FINISH_BUTTON)

    def enter_url(self, url: str):
        amount_input = self.find(self.locators.URL_INPUT)
        amount_input.clear()
        amount_input.send_keys(url)

    def get_api_key_field(self):
        return self.is_visible(self.locators.ADD_API_KEY)

    def change_good_category(self):
        self.click(self.locators.GOOD_DROPDOWN)

    def choose_good_category(self):
        self.click(self.locators.GOOD_AUTO)

    def get_choosed_good_category(self):
        return self.find(self.locators.GOOD_EXAMPLE).text

    def is_catalog_table_created(self) -> bool:
        return self.is_visible(self.locators.CATALOGS_TABLE)
    
    def is_catalog_page_opened(self) -> bool:
        return self.is_visible(self.locators.CATALOG_PAGE_HISTORY)

    def open_ecomm(self):
        self.click(self.locators.ECOMM_MENU_BUTTON)

    def is_catalogue_in_table(self, title):
        self.find(self.locators.CREATE_CATALOG_COMMON_BUTTON)
        catalogs = self.driver.find_elements(*self.locators.CATALOG_TITLE)
        
        for t in [cat.text for cat in catalogs]:
            if title in t:
                return True
        return False
    
    def open_catalog(self, title):
        self.find(self.locators.CREATE_CATALOG_COMMON_BUTTON)
        catalogs = self.driver.find_elements(*self.locators.CATALOG_TITLE)
        for cat in catalogs:
            if title in cat.text:
                cat.click()
                return

        assert False

    def is_catalogue_active(self, title):
        self.find(self.locators.CREATE_CATALOG_COMMON_BUTTON)
        catalogs = self.driver.find_elements(*self.locators.CATALOG_TITLE)
        statuses = self.driver.find_elements(*self.locators.CATALOG_STATUS)
        index = -1
        for i, cat in enumerate(catalogs):
            if title in cat.text:
                index = i
        
        assert index != -1
        return "Активный" in statuses[index].text
    
    def is_product_in_table(self, title):
        return self.is_visible(self.locators.PRODUCT_CARD(title))
    
    def open_settings(self):
        self.click(self.locators.BUTTON("Настройки"))
    
    def click_delele_catalog(self):
        time.sleep(1)
        self.click(self.locators.BUTTON("Удалить каталог"))
    
    def is_confirm_delete_visible(self):
        return self.is_visible(self.locators.MODAL_CONFIRM_DELETE, timeout=50)
    
    def is_confirm_delete_invisible(self):
        return self.is_invisible(self.locators.MODAL_CONFIRM_DELETE)
    
    def confirm_delete(self):
        self.click(self.locators.BUTTON("Удалить"))

    def upload_file(self, file):
        input = self.find(self.locators.FILE_INPUT)
        input.send_keys(os.path.abspath(file))

    def open_groups(self):
        self.click(self.locators.GROUPS_TAB)

    def create_filter_group(self):
        self.click(self.locators.CREATE_GROUP, timeout=10)
        self.find_all(self.locators.GROUP_DROPDOWN)[0].click()

    def set_price_higher_than(self, price):
        input = self.find(self.locators.CONDITION_INPUT, timeout=2)
        input.clear()
        input.send_keys(price)

    def set_group_name(self, name):
        input = self.find(self.locators.GROUP_NAME_INPUT)
        input.clear()
        input.send_keys(name)

    def open_group(self, name):
        self.click(self.locators.GROUP_HEADER(name))

    def get_products_titles(self):
        return map(lambda p: p.text, self.find_all(self.locators.PRODUCT_TITLE))