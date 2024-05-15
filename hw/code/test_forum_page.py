from base_case import BaseCase


class TestForumPage(BaseCase):

    def test_content(self, forum_page):
        assert forum_page.check_title() == 'Форум идей'
        assert forum_page.check_subtitle() == 'Голосуйте за лучшие идеи или предлагайте свои'

    def test_search_not_found(self, forum_page):
        assert not forum_page.is_visible_nf()
        forum_page.fill_search('-1')
        forum_page.wait_nf()
        assert forum_page.is_visible_nf()

    def test_search_drop_filters(self, forum_page):
        forum_page.fill_search('-1')
        forum_page.wait_nf()
        assert forum_page.is_visible_nf()
        forum_page.click_drop_filtres()
        assert not forum_page.is_visible_nf()

    def test_open_theme_dropdown(self, forum_page):
        forum_page.open_filter_dropdown('Любая тема')
        assert forum_page.filter_dropdown_contain_items(forum_page.THEMES)

    def test_open_status_dropdown(self, forum_page):
        forum_page.open_status_dropdown()
        assert forum_page.filter_dropdown_contain_items(forum_page.STATUSES)

    def test_open_comments(self, forum_page):
        assert forum_page.open_comments()
