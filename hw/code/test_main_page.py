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

    def test_see_all_link(self, main_page):
        main_page.click(MainPageLocators.SEE_ALL_LINK)
        assert self.is_opened('https://ads.vk.com/cases')

    @pytest.mark.skip(reason="работает только в crome")
    def test_teach_web(self, main_page):
        assert main_page.find(MainPageLocators.TEACH_WEB_TITLE).text == 'Обучающие вебинары'
        assert main_page.find(MainPageLocators.TEACH_WEB_SUBTITLE).text == 'Эксперты VK и наши партнеры рассказывают, как эффективно использовать технологии VK Рекламы'
        main_page.scroll_and_click(MainPageLocators.TEACH_WEB_BUTTON)
        assert self.is_opened('https://ads.vk.com/events')
