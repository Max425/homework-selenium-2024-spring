from ui.locators.forum_page_locators import ForumPageLocators
from ui.pages.base_page import BasePage


class ForumPage(BasePage):
    url = 'https://ads.vk.com/upvote'

    THEMES = ['Лидформы', 'Сообщества', 'Форум идей', 'Сайты', 'Каталог товаров', 'Мобильные приложения', 'Другое']
    STATUSES = ['Голосование', 'Уже в работе', 'Реализована', 'Отклонено']

    def get_first_idea_id(self):
        date_and_id = self.find(ForumPageLocators.IDEA_DATE_AND_ID).text.split()
        return date_and_id[len(date_and_id) - 1]

    def open_filter_dropdown(self, filter_name):
        self.click(ForumPageLocators.SELECTED_FILTER(filter_name))

    def filter_dropdown_contain_items(self, item_names):
        return all(self.find(ForumPageLocators.FILTER_OPTION(item_name)) for item_name in item_names)
