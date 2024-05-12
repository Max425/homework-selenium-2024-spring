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

    # slider
    BULLET_BUTTON = (By.XPATH, "//*[contains(@class, 'Bullets_box__')]")
    SLIDER_TITLE = (By.XPATH, "//*[contains(@class, 'MainSlider_active__')]//p")
    SLIDER_SUBTITLE = (By.XPATH, "//*[contains(@class, 'MainSlider_description__')]//p")

    @staticmethod
    def SLIDER_BUTTON(url):
        return By.XPATH, f"//a[contains(@class, 'MainSlider_button__') and contains(@href, '{url}')]"
