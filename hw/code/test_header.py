import pytest

from base_case import BaseCase
from ui.pages.main_page import MainPage


class TestHeader(BaseCase):

    @pytest.mark.parametrize("locator,url", [
        (MainPage.vk_ads_logo, 'https://ads.vk.com/'),
        (MainPage.cabinet_button, 'https://id.vk.com/auth'),
        (MainPage.header_help, 'https://ads.vk.com/help'),
        (MainPage.news_link, 'https://ads.vk.com/news'),
        (MainPage.cases_link, 'https://ads.vk.com/cases'),
        (MainPage.forum_link, 'https://ads.vk.com/upvote')
    ])
    def test_go_to_sections(self, main_page, locator, url):
        locator(main_page)
        assert self.is_opened(url)
