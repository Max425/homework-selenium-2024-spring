import time
from base_case import BaseCase
from ui.locators.forum_page_locators import ForumPageLocators


class TestUpvotePage(BaseCase):

    def test_content(self, forum_page):
        assert forum_page.find(ForumPageLocators.TITLE).text == 'Форум идей'
        assert forum_page.find(
            ForumPageLocators.SUBTITLE).text == 'Голосуйте за лучшие идеи или предлагайте свои'

    def test_upvote_modal_page_became_visible(self, forum_page):
        forum_page.click(ForumPageLocators.ADD_IDEA)
        assert forum_page.is_visible(ForumPageLocators.UPVOTE_MODAL_PAGE)
        forum_page.click(ForumPageLocators.OK_PON)
        assert not forum_page.is_visible(ForumPageLocators.UPVOTE_MODAL_PAGE)

    def test_search_not_found(self, forum_page):
        assert not forum_page.is_visible(ForumPageLocators.NOT_FOUND)
        forum_page.fill_field(ForumPageLocators.SEARCH_FIELD, '-1')
        time.sleep(1)
        assert forum_page.is_visible(ForumPageLocators.NOT_FOUND)

    def test_search_drop_filters(self, forum_page):
        forum_page.fill_field(ForumPageLocators.SEARCH_FIELD, '-1')
        time.sleep(1)
        assert forum_page.is_visible(ForumPageLocators.NOT_FOUND)
        forum_page.click(ForumPageLocators.DROP_FILTERS)
        assert not forum_page.is_visible(ForumPageLocators.NOT_FOUND)

    def test_open_theme_dropdown(self, forum_page):
        forum_page.open_filter_dropdown('Любая тема')
        assert forum_page.filter_dropdown_contain_items(forum_page.THEMES)

    def test_open_status_dropdown(self, forum_page):
        forum_page.click(ForumPageLocators.CANCEL_FILTER_BUTTON)
        forum_page.open_filter_dropdown('Любой статус')
        assert forum_page.filter_dropdown_contain_items(forum_page.STATUSES)

    def test_open_comments(self, forum_page):
        forum_page.click(ForumPageLocators.COMMENT_BUTTON)
        assert forum_page.is_visible(ForumPageLocators.COMMENT_ITEM)
