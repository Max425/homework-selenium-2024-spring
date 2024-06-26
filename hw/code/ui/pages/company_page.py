import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.company_page_locators import CompanyPageLocators


class CompanyPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CompanyPageLocators()

    SECOND_STAGE_NAME = 'Группы объявлений'
    THIRD_STAGE_NAME = 'Объявления'

    def click_delete(self):
        self.click(self.locators.SELECT_DELETE)

    def click_context_menu(self):
        self.click(self.locators.CONTEXT_MENU)

    def click_select_actions(self):
        self.click(self.locators.SELECT_ACTIONS)

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
        except TimeoutException:
            pass

    def click_create_company(self):
        self.click(self.locators.CREATE_COMPANY_BUTTON)

    def select_site(self):
        self.click(self.locators.SITE)

    def site_input_is_visible(self) -> bool:
        return self.is_visible(self.locators.SITE_INPUT)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_continue_button(self):
        continue_button = self.wait_until(EC.visibility_of_element_located(self.locators.CONTINUE_BUTTON), 10)
        continue_button.click()

    def enter_site_url(self, url: str):
        elem = self.find(self.locators.SITE_INPUT)
        elem.clear()
        elem.send_keys(url)
        elem.send_keys(Keys.ENTER)

    def options_is_visible(self) -> bool:
        return (self.is_visible(self.locators.GOAL_DROPDOWN)
                and self.is_visible(self.locators.STRATEGY_DROPDOWN)
                and self.is_visible(self.locators.BUDGET_INPUT)
                and self.is_visible(self.locators.DATES))

    def get_start_date(self) -> str | None:
        return self.find(self.locators.START_DATE).get_attribute('value')

    def enter_budget_amount(self, amount: str | int):
        elem = self.find(self.locators.BUDGET_INPUT)
        elem.clear()
        elem.send_keys(amount)
        time.sleep(1)

    def is_active_stage(self, stage_name: str):
        try:
            self.find(self.locators.ACTIVE_STAGE(stage_name))
            return True
        except TimeoutException:
            return False

    def select_regions(self):
        region_selection = self.wait_until(EC.visibility_of_element_located(self.locators.REGION_QUICK_SELECTION), 10)
        region_selection.click()

    def get_panel_title(self) -> str:
        return self.find(self.locators.PANEL_TITLE).text

    def click_media_button(self):
        self.click(self.locators.MEDIA_BUTTON)

    def select_image(self):
        self.click(self.locators.GENERATED_IMAGES_TAB)
        self.click(self.locators.IMAGE_ITEM)

    def is_image_selected(self) -> bool:
        try:
            self.find(self.locators.SELECTED_IMAGE)
            return True
        except TimeoutException:
            return False

    def enter_title_and_description(self, title: str, description: str):
        elem = self.find(self.locators.TITLE)
        elem.clear()
        elem.send_keys(title)

        elem = self.find(self.locators.DESCRIPTION)
        elem.clear()
        elem.send_keys(description)

    def get_preview_title(self) -> str:
        return self.find(self.locators.PREVIEW_TITLE).text

    def get_preview_description(self) -> str:
        return self.find(self.locators.PREVIEW_DESCRIPTION).text

    def click_publish_button(self):
        self.click(self.locators.PUBLISH_BUTTON)

    def click_neuro_image(self):
        self.click(self.locators.NEURO_IMAGE)

    def click_neuro_image_for_media(self):
        self.scroll_and_click(self.locators.NEURO_IMAGE_FOR_MEDIA)

    def click_add_image(self):
        self.click(self.locators.ADD_IMAGE)


    def click_image(self):
        self.click(self.locators.IMAGE)

    def click_public_company(self):
        self.click(self.locators.PUBLIC_COMPANY)

    def click_create(self):
        self.click(self.locators.CREATE_BUTTON)

