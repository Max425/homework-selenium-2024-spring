import pytest

from base_case import BaseCase
from ui.locators.main_page_locators import MainPageLocators


class TestMainPage(BaseCase):

    @pytest.mark.parametrize("page_num,title,subtitle,url", [
        (0, 'До 10 000₽ бонусов на первую кампанию',
         'Перейдите на страницу акции и зарегистрируйтесь в VK Рекламе, чтобы воспользоваться специальными условиями',
         '/promo/firstbonus'),
        (1, 'Привлекать клиентов с VK Рекламой — легко!',
         'Автоматически создадим креативы, предложим настройки и покажем рекламу заинтересованным пользователям проектов VK',
         '/hq')
    ])
    def test_slides(self, main_page, page_num, title, subtitle, url):
        for i in range(page_num):
            main_page.click(MainPageLocators.BULLET_BUTTON)
        assert main_page.find(MainPageLocators.SLIDER_TITLE).text in title
        assert main_page.find(MainPageLocators.SLIDER_SUBTITLE).text in subtitle
        main_page.click(MainPageLocators.SLIDER_BUTTON(url))
        assert self.is_opened(url)
