import pytest

from base_case import BaseCase


class TestHeader(BaseCase):
    def test_go_to_home(self, main_page):
        main_page.click_vk_ads_logo()
        assert self.is_opened(main_page.url)

    def test_go_to_auth(self, main_page):
        main_page.click_nav_cabinet_button()
        assert self.is_opened('https://id.vk.com/auth')

    @pytest.mark.parametrize("name,url", [
        ('Справка', 'https://ads.vk.com/help'),
        ('Новости', 'https://ads.vk.com/news'),
        ('Кейсы', 'https://ads.vk.com/cases'),
        ('Форум идей', 'https://ads.vk.com/upvote'),
        ('Монетизация', 'https://ads.vk.com/partner')
    ])
    def test_go_to_sections(self, main_page, name, url):
        main_page.click_nav_item(name)
        assert self.is_opened(url)

