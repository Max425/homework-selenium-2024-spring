from selenium.webdriver.common.by import By


class ForumPageLocators:
    TITLE = (By.XPATH, "//*[@data-test-id=summary-title-ads]")
    SUBTITLE = (By.XPATH, "//*[contains(@class, 'Summary_description__')]")

    ADD_IDEA = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Предложить идею']")
    OK_PON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Ок, понятно']")
    UPVOTE_MODAL_PAGE = (By.XPATH,"//*[contains(@class, 'vkuiModalCardBase__header') and text()='Как стать участником форума?']")

    COMMENT_BUTTON = (By.XPATH, "//*[contains(@class, 'ButtonComment_button__')]")
    COMMENT_ITEM = (By.XPATH, "//*[contains(@class, 'Comment_cell__')]")

    COMMENT_COUNTER = (
        By.XPATH,
        "//*[contains(@class, 'ButtonComment_button__')]//span[contains(@class, 'vkuiButton__content')]"
    )

    SEARCH_FIELD = (By.XPATH, "//*[contains(@class, 'vkuiSearch__input')]")

    IDEA_TITLE = (By.XPATH, "//*[contains(@class, 'Idea_title__')]")
    IDEA_DATE_AND_ID = (By.XPATH, "//*[contains(@class, 'vkuiSimpleCell__text')]")
    IDEA_THEME = (By.XPATH, "//*[contains(@class, 'Tag_tag__')]")
    IDEA_STATUS = (By.XPATH, "//*[contains(@class, 'Status_wrap__')]")

    CANCEL_FILTER_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiIcon--cancel')]")
    NOT_FOUND = (By.XPATH, "//*[contains(@class, 'vkuiPlaceholder')]")
    DROP_FILTERS = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Сбросить фильтры']")

    CARD_LINK = (By.XPATH, "//*[href='/upvote/40']")

    @staticmethod
    def FILTER_OPTION(option_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption__') and text()='{option_name}']"
