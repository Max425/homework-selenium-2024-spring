from selenium.webdriver.common.by import By


class MainPageLocators:
    # header
    CABINET_BUTTON = (By.XPATH, "//*[contains(@class, 'NavigationVKAds_right__')]/a[contains(@class, 'ButtonCabinet_primary__')]")
    HEADER_HELP = (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='Справка']")
    NEWS_LINK = (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='Новости']")
    CASES_LINK = (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='Кейсы']")
    FORUM_LINK = (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='Форум идей']")
    MONEY_LINK = (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='Монетизация']")
    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home')]")

    # content
    @staticmethod
    def SLIDER_BUTTON(url):
        return By.XPATH, f"//a[contains(@class, 'MainSlider_button') and contains(@href, '{url}')]"

    SEE_ALL_LINK = (By.XPATH, "//*[contains(@class, 'styles_all')]")
    CASE_ITEM = (By.XPATH, "//*[contains(@class, 'Case_content')]")
    CASE_ITEM_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title')]")

    WEBINAR_ITEM = (By.XPATH, "//*[contains(@class, 'GetStarted_wrapper')]")
