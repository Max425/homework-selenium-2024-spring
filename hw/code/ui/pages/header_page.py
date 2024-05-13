from ui.pages.base_page import BasePage
from ui.locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'

    def click_vk_logo_button(self):
        self.click(HeaderPageLocators.VK_LOGO_BUTTON)

    def click_change_account_button(self):
        self.click(HeaderPageLocators.CHANGE_ACCOUNT_BUTTON)

    def click_all_cabinets_button(self):
        self.click(HeaderPageLocators.ALL_CABINETS_BUTTON)

    def click_wallet_button(self):
        self.click(HeaderPageLocators.WALLET_BUTTON)

    def is_modal_wallet_visible(self):
        return self.is_visible(HeaderPageLocators.REPLENISH_WALLET_BUTTON)
    
    def click_notifications_button(self):
        self.click(HeaderPageLocators.NOTIFICATIONS_BUTTON)

    def is_modal_notifications_visible(self):
        return self.is_visible(HeaderPageLocators.NOTIFICATIONS_CONTENT)
    
    def click_user_avatar_button(self):
        self.click(HeaderPageLocators.USER_AVATAR_BUTTON)

    def click_quit_button(self):
        self.click(HeaderPageLocators.QUIT_BUTTON)
