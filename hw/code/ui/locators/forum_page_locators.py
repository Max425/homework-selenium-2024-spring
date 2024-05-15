from selenium.webdriver.common.by import By


class ForumPageLocators:
    TITLE = (By.XPATH, "//*[contains(@class, 'Summary_title__')]")
    SUBTITLE = (By.XPATH, "//*[contains(@class, 'Summary_description__')]")

    ADD_IDEA = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Предложить идею']")
    OK_PON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Ок, понятно']")
    UPVOTE_MODAL_PAGE = (By.XPATH,"//*[contains(@class, 'vkuiModalCardBase__header') and text()='Как стать участником форума?']")

    COMMENT_BUTTON = (By.XPATH, "//*[contains(@class, 'ButtonComment_button__')]")
    COMMENT_ITEM = (By.XPATH, "//*[contains(@class, 'Comment_cell__')]")

    SEARCH_FIELD = (By.XPATH, "//*[contains(@class, 'vkuiSearch__input')]")

    CANCEL_FILTER_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiIcon--cancel')]")
    NOT_FOUND = (By.XPATH, "//*[contains(@class, 'vkuiPlaceholder')]")
    DROP_FILTERS = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Сбросить фильтры']")

    @staticmethod
    def SELECTED_FILTER(filter_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiSelect__title') and text()='{filter_name}']"

    @staticmethod
    def FILTER_OPTION(option_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption__') and text()='{option_name}']"
