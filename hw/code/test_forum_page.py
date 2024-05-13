import time
from base_case import BaseCase
from ui.locators.forum_page_locators import ForumPageLocators


class TestUpvotePage(BaseCase):
    def test_upvote_modal_page_became_visible(self, forum_page):
        forum_page.click(ForumPageLocators.ADD_IDEA)
        assert forum_page.is_visible(ForumPageLocators.UPVOTE_MODAL_PAGE)

    def test_open_comments(self, forum_page):
        forum_page.click(ForumPageLocators.COMMENT_BUTTON)
        assert forum_page.is_visible(ForumPageLocators.COMMENT_ITEM)

    def test_search_by_title(self, forum_page):
        word = 'видео'
        forum_page.fill_field(ForumPageLocators.SEARCH_FIELD, word)
        time.sleep(1)
        assert word in forum_page.find(ForumPageLocators.IDEA_TITLE).text

    def test_search_by_id(self, forum_page):
        idea_id = '40'
        forum_page.fill_field(ForumPageLocators.SEARCH_FIELD, idea_id)
        time.sleep(1)
        assert idea_id == forum_page.get_first_idea_id()

    def test_open_theme_dropdown(self, forum_page):
        forum_page.open_filter_dropdown('Любая тема')
        assert forum_page.filter_dropdown_contain_items(forum_page.THEMES)

    def test_open_status_dropdown(self, forum_page):
        forum_page.click(ForumPageLocators.CANCEL_FILTER_BUTTON)
        forum_page.open_filter_dropdown('Любой статус')
        assert forum_page.filter_dropdown_contain_items(forum_page.STATUSES)

    def test_filter_theme(self, forum_page):
        forum_page.open_filter_dropdown('Любая тема')

        theme = 'Лидформы'
        forum_page.select_filter(theme)
        assert forum_page.find(ForumPageLocators.IDEA_THEME).text == theme

    def test_filter_status(self, forum_page):
        forum_page.click(ForumPageLocators.CANCEL_FILTER_BUTTON)
        forum_page.open_filter_dropdown('Любой статус')

        status = 'Уже в работе'
        forum_page.select_filter(status)
        assert forum_page.find(ForumPageLocators.IDEA_STATUS).text == status