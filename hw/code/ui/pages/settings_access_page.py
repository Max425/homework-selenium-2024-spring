from ui.pages.base_page import BasePage
from ui.locators.settings_access_page_locators import SettingsAccessPageLocators


class SettingsAccessPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/access'

    def click_more_href(self):
        self.click(SettingsAccessPageLocators.MORE_HREF)

    def is_save_button_visible(self) -> bool:
        return self.is_visible(SettingsAccessPageLocators.SAVE_BUTTON)

    def click_add_cabinet_button(self):
        self.click(SettingsAccessPageLocators.ADD_CABINET_BUTTON)
