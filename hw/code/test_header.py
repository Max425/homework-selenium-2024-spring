import pytest

from base_case import BaseCase
from ui.locators.main_page_locators import MainPageLocators


class TestHeader(BaseCase):

    @pytest.mark.parametrize("locator,url", [
        (MainPageLocators.VK_ADS_LOGO, 'https://ads.vk.com/'),
        (MainPageLocators.CABINET_BUTTON, 'https://id.vk.com/auth'),
        (MainPageLocators.HEADER_HELP, 'https://ads.vk.com/help'),
        (MainPageLocators.NEWS_LINK, 'https://ads.vk.com/news'),
        (MainPageLocators.CASES_LINK, 'https://ads.vk.com/cases'),
        (MainPageLocators.FORUM_LINK, 'https://ads.vk.com/upvote')
       # (MainPageLocators.MONEY_LINK, 'https://ads.vk.com/partner')
    ])
    def test_go_to_sections(self, main_page, locator, url):
        main_page.click(locator)
        assert self.is_opened(url)
