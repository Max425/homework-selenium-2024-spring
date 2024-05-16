from ui.locators.forum_page_locators import ForumPageLocators
from ui.pages.base_page import BasePage


class ForumPage(BasePage):
    url = 'https://ads.vk.com/upvote'

    THEMES = ['Лидформы', 'Сообщества', 'Форум идей', 'Сайты', 'Каталог товаров', 'Мобильные приложения', 'Другое']
    STATUSES = ['Голосование', 'Уже в работе', 'Реализована', 'Отклонено']

    def check_title(self):
        return self.find(ForumPageLocators.TITLE).text

    def check_subtitle(self):
        return self.find(ForumPageLocators.SUBTITLE).text


    def open_filter_dropdown(self, filter_name):
        self.click(ForumPageLocators.SELECTED_FILTER(filter_name))

    def filter_dropdown_contain_items(self, item_names):
        return all(self.find(ForumPageLocators.FILTER_OPTION(item_name)) for item_name in item_names)

    def is_visible_nf(self):
        return self.is_visible(ForumPageLocators.NOT_FOUND)

    def fill_search(self, val):
        return self.fill_field(ForumPageLocators.SEARCH_FIELD, val)

    def wait_nf(self):
        return self.find(ForumPageLocators.NOT_FOUND)

    def click_drop_filtres(self):
        return self.scroll_and_click(ForumPageLocators.DROP_FILTERS)

    def open_comments(self):
        self.scroll_and_click(ForumPageLocators.COMMENT_BUTTON)
        return self.is_visible(ForumPageLocators.COMMENT_ITEM)

    def open_status_dropdown(self):
        self.scroll_and_click(ForumPageLocators.CANCEL_FILTER_BUTTON)
        self.open_filter_dropdown('Любой статус')
