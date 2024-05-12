from ui.pages.base_page import BasePage
from ui.locators.cases_page_locators import CasesPageLocators


class CasesPage(BasePage):
    url = 'https://ads.vk.com/cases'

    def get_page_title(self):
        return self.find(CasesPageLocators.PAGE_TITLE).text

    def get_case_title(self) -> str:
        return self.find(CasesPageLocators.CASE_TITLE).text

    def click_case_item(self):
        self.click(CasesPageLocators.CASE_ITEM)