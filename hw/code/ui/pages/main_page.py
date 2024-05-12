from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    url = 'https://ads.vk.com/'

    def click_vk_ads_logo(self):
        self.click(MainPageLocators.VK_ADS_LOGO)

    def click_nav_item(self, item_name: str):
        self.click(MainPageLocators.NAV_ITEM(item_name))

    def click_nav_cabinet_button(self):
        self.click(MainPageLocators.NAV_CABINET_BUTTON)

    def click_vk_business_logo(self):
        self.scroll_and_click(MainPageLocators.VK_BUSINESS_LOGO)

    def get_selected_language_from_footer(self) -> str:
        return self.find(MainPageLocators.FOOTER_SELECTED_LANGUAGE).text

    def open_language_dropdown(self):
        self.scroll_and_click(MainPageLocators.FOOTER_LANGUAGE_DROPDOWN)

    def language_dropdown_contain_items(self, item_names) -> bool:
        for item_name in item_names:
            item = self.find(MainPageLocators.FOOTER_LANGUAGE_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

            return True

    def change_language(self, language: str):
        self.open_language_dropdown()
        self.click(MainPageLocators.FOOTER_LANGUAGE_DROPDOWN_ITEM(language))

    def click_social_media_item(self, social_media_url: str):
        self.scroll_and_click(MainPageLocators.FOOTER_SOCIAL_MEDIA_ITEM(social_media_url))

    def click_footer_about(self):
        self.scroll_and_click(MainPageLocators.FOOTER_ABOUT)

    def get_slide_title(self) -> str:
        return self.find(MainPageLocators.SLIDER_TITLE).text

    def change_slide(self):
        self.click(MainPageLocators.NONACTIVE_CIRCLE)

    def click_slider_cabinet_button(self):
        self.click(MainPageLocators.SLIDER_BUTTON('/hq'))

    def click_slider_bonus_button(self):
        self.click(MainPageLocators.SLIDER_BUTTON('/promo/firstbonus'))

    def click_see_all(self):
        self.click(MainPageLocators.SEE_ALL_LINK)

    def click_case_item(self):
        self.click(MainPageLocators.CASE_ITEM)

    def get_case_title(self) -> str:
        return self.find(MainPageLocators.CASE_ITEM_TITLE).text

    def click_webinar_item(self):
        self.scroll_and_click(MainPageLocators.WEBINAR_ITEM)
