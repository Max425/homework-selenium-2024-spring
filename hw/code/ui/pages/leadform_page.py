from ui.pages.base_page import BasePage
from ui.locators.leadform_page_locators import LeadformPageLocators
import time


class LeadformPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'

    def click_create_leadform_button(self):
        self.click(LeadformPageLocators.CREATE_LEADFORM_BUTTON)

    def fill_leadform_name_field(self, name: str):
        self.fill_field(LeadformPageLocators.INPUT_NAME_LEAD_FORM, name)

    def fill_company_name_field(self, name: str):
        self.fill_field(LeadformPageLocators.INPUT_NAME_COMPANY, name)

    def fill_leadform_title_field(self, title: str):
        self.fill_field(LeadformPageLocators.INPUT_TITLE, title)

    def fill_leadform_description_field(self, description: str):
        self.fill_field(LeadformPageLocators.INPUT_DESCRIPTION, description)

    def click_download_and_choose_logo_button(self):
        self.click(LeadformPageLocators.DOWNLOAD_LOGO)
        self.click(LeadformPageLocators.CHOOSE_LOGO)

    def click_save_button(self):
        self.click(LeadformPageLocators.CONTINUE_BUTTON)

    def click_cancel_button(self):
        self.click(LeadformPageLocators.CANCEL_BUTTON)

    def fill_leadform_legal_name_field(self, name: str):
        self.fill_field(LeadformPageLocators.INPUT_LEGAL_NAME_COMPANY, name)

    def fill_leadform_legal_adress_field(self, adress: str):
        self.fill_field(LeadformPageLocators.INPUT_LEGAL_ADRESS_COMPANY, adress)

    def is_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadformPageLocators.CONTINUE_BUTTON)
    
    def is_leadform_page_closed(self) -> bool:
        return not self.is_visible(LeadformPageLocators.CONTINUE_BUTTON)
    
    def is_question_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadformPageLocators.ADD_CONTACTS_BUTTON)
    
    def is_result_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadformPageLocators.ADD_SITE_BUTTON)
    
    def is_settings_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadformPageLocators.INPUT_LEGAL_NAME_COMPANY)
    
    def is_leadform_in_list_exists(self, name: str) -> bool:
        return self.is_visible(LeadformPageLocators.SELECT_FROM_LEADFORM_LIST(name))
    
    def click_delete_leadform_button(self, name: str):
        self.hover_elem(LeadformPageLocators.SELECT_FROM_LEADFORM_LIST(name))
        self.click(LeadformPageLocators.DELETE_LEADFORM_BUTTON(name))
        self.click(LeadformPageLocators.CONTINUE_BUTTON)

    def fill_find_leadform_field(self, name: str):
        self.fill_field(LeadformPageLocators.INPUT_FIND_LEADFORM, name)

    def click_editing_leadform(self, name: str):
        self.hover_elem(LeadformPageLocators.SELECT_FROM_LEADFORM_LIST(name))
        self.click(LeadformPageLocators.EDIT_LEADFORM_BUTTON(name))

    def get_leadform_name(self):
        return self.find(LeadformPageLocators.INPUT_NAME_LEAD_FORM).text

    def get_leadform_company_name(self):
        return self.find(LeadformPageLocators.INPUT_NAME_COMPANY).text
    
    def get_leadform_title(self):
        return self.find(LeadformPageLocators.INPUT_TITLE).text
    
    def get_leadform_description(self):
        return self.find(LeadformPageLocators.INPUT_DESCRIPTION).text
    
    def get_leadform_legal_name(self):
        return self.find(LeadformPageLocators.INPUT_LEGAL_NAME_COMPANY).text
    
    def get_leadform_legal_adress(self):
        return self.find(LeadformPageLocators.INPUT_LEGAL_ADRESS_COMPANY).text