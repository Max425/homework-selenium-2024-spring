from ui.pages.base_page import BasePage
from ui.locators.menu_page_locators import MainPageLocators


class MenuPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'

    def click_campaings_button(self):
        self.click(MainPageLocators.CAMPAIGNS_BUTTON)

    def click_audience_button(self):
        self.click(MainPageLocators.AUDIENCE_BUTTON)

    def click_budget_button(self):
        self.click(MainPageLocators.BUDGET_BUTTON)

    def click_ecomm_catalogs_button(self):
        self.click(MainPageLocators.ECOMM_CATALOGS_BUTTON)

    def click_pixels_button(self):
        self.click(MainPageLocators.PIXELS_BUTTON)

    def click_apps_button(self):
        self.click(MainPageLocators.APPS_BUTTON)

    def click_leadads_button(self):
        self.click(MainPageLocators.LEADADS_BUTTON)

    def click_training_button(self):
        self.click(MainPageLocators.TRAINING_BUTTON)

    def is_modal_training_visible(self):
        return self.is_visible(MainPageLocators.TRAINING_MODAL_CONTENT)
    
    def click_settings_button(self):
        self.click(MainPageLocators.SETTINGS_BUTTON)