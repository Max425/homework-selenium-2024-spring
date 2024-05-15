import pytest
from base_case import BaseCase


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
            main_page.bullet_button()
        assert main_page.slider_title() in title
        assert main_page.slider_subtitle() in subtitle
        main_page.slider_button(url)
        assert self.is_opened(url)

    def test_see_all_link(self, main_page):
        main_page.see_all_link()
        assert self.is_opened('https://ads.vk.com/cases')

    def test_teach_web(self, main_page):
        assert main_page.teach_web_title() == 'Обучающие вебинары'
        assert main_page.teach_web_subtitle() == 'Эксперты VK и наши партнеры рассказывают, как эффективно использовать технологии VK Рекламы'
        main_page.teach_web_button()
        assert self.is_opened('https://ads.vk.com/events')

    def test_news_section(self, main_page):
        assert main_page.news_section() == 'Новости'
        assert main_page.news_title() == 'Составляйте портрет аудитории сайта в VK Рекламе'
        main_page.news_button()
        assert self.is_opened('https://ads.vk.com/news/portret-auditorii-sayta-vk-reklama')
