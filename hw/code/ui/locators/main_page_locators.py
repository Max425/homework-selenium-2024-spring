from selenium.webdriver.common.by import By


class MainPageLocators:
    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home')]")

    NAV_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAds_right')]/a[contains(@class, 'ButtonCabinet_primary')]"
    )

    FOOTER_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Footer_leftContent')]/a[contains(@class, 'ButtonCabinet_primary')]"
    )

    @staticmethod
    def NAV_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_') and text()='{item_name}']"

    @staticmethod
    def SLIDER_BUTTON(url):
        return By.XPATH, f"//a[contains(@class, 'MainSlider_button') and contains(@href, '{url}')]"

    SEE_ALL_LINK = (By.XPATH, "//*[contains(@class, 'styles_all')]")
    CASE_ITEM = (By.XPATH, "//*[contains(@class, 'Case_content')]")
    CASE_ITEM_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title')]")

    WEBINAR_ITEM = (By.XPATH, "//*[contains(@class, 'GetStarted_wrapper')]")
