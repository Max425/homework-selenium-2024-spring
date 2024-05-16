from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    url = 'https://ads.vk.com/'

    def vk_ads_logo(self):
        return self.click(MainPageLocators.VK_ADS_LOGO)

    def cabinet_button(self):
        return self.click(MainPageLocators.CABINET_BUTTON)

    def header_help(self):
        return self.click(MainPageLocators.HEADER_HELP)

    def news_link(self):
        return self.click(MainPageLocators.NEWS_LINK)

    def cases_link(self):
        return self.click(MainPageLocators.CASES_LINK)

    def forum_link(self):
        return self.click(MainPageLocators.FORUM_LINK)

    def bullet_button(self):
        return self.click(MainPageLocators.BULLET_BUTTON)

    def slider_title(self):
        return self.find(MainPageLocators.SLIDER_TITLE).text

    def slider_subtitle(self):
        return self.find(MainPageLocators.SLIDER_SUBTITLE).text

    def slider_button(self, url):
        return self.click(MainPageLocators.SLIDER_BUTTON(url))

    def see_all_link(self):
        return self.click(MainPageLocators.SEE_ALL_LINK)

    def teach_web_title(self):
        return self.find(MainPageLocators.TEACH_WEB_TITLE).text

    def teach_web_subtitle(self):
        return self.find(MainPageLocators.TEACH_WEB_SUBTITLE).text

    def teach_web_button(self):
        return self.scroll_and_click(MainPageLocators.TEACH_WEB_BUTTON)

    def news_section(self):
        return self.find(MainPageLocators.NEWS_SECTION).text

    def news_title(self):
        return self.find(MainPageLocators.NEWS_TITLE).text

    def news_button(self):
        return self.scroll_and_click(MainPageLocators.NEWS_BUTTON)
