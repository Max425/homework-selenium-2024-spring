from selenium.webdriver.common.by import By


class AudiencePageLocators:
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")

    AUDIENCE_NAME_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiInput__el')]")
    ERROR = (By.XPATH, "//*[@role='alert']")

    ADD_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']")

    @staticmethod
    def MODAL(title):
        return (
            By.XPATH,
            f"//*[contains(@class, 'ModalSidebarPage_container') and contains(div/h2, '{title}')]"
        )

    @staticmethod
    def SOURCE_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'SourceTypeSelector_button__')]//*[text()='{item_name}']"

    KEY_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_textarea__')]/textarea")

    MODAL_SUBMIT_BUTTON = (By.XPATH,
                           "//div[contains(@class, 'ModalRoot_componentWrapper')and .//h2[text()='Ключевые фразы']]//button[@type='submit']")
    SOURCE_CARD_CONTENT = (
        By.XPATH,
        "//*[contains(@class, 'SourcesList_wrapper__')]//*[contains(@class, 'InfoRow_content__')]"
    )

    CREATED_AUDIENCE_TITLE = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/h5")

    @staticmethod
    def MODAL_FIELD(label):
        return By.XPATH, f"//div[contains(h5, '{label}')]//textarea"

    @staticmethod
    def MODAL_INPUT(label):
        return By.XPATH, f"//div[contains(h5, '{label}')]//input[contains(@class, 'vkuiTypography')]"

    AUDIENCE_CREATE = (By.XPATH, f"//*[@data-testid='submit']")

    @staticmethod
    def AUDIENCE_CREATED(label):
        return By.XPATH, f"//*[contains(@class, 'BaseTable__row')]//div[contains(h5, '{label}')]"
    
    AUDIENCE_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiIcon--check_box_off_20')]")
    AUDIENCE_DELETE = (By.XPATH, f"//*[@data-testid='remove-items-button']")
    AUDIENCE_APROVE_DELETING = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")
    
    GROUP_LINK_INPUT = (By.XPATH, f"//*[@placeholder='Введите название сообщества']")
    GROUP_SELECT = (By.XPATH, f"//*[@id='react-collapsed-toggle-1']")
    GROUP_OPTION = (By.XPATH, f"//*[@id='react-collapsed-panel-1']")
    SELECTED_GROUP = (By.XPATH, "//*[contains(@class, 'Selected_item__')]//*[contains(@class, 'Selected_name__')]")
    
    ADD_MANY_GROUPS_BTN = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить списком']")
    SELECT_VK_GROUPS = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Сообщества ВКонтакте']")
    SELECT_MANY_GROUPS_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiPanelHeader__content-in') and text()='Добавление списка']")
    ADD_MANY_GROUPS_SUCCESS = (By.XPATH, "//*[contains(@class, 'AddTextListCard_status__')]")
    COMPLETE_ADD_MANY_GROUPS_BTN = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить']")
    CLOSE_BTN = (By.XPATH, f"//*[@aria-label='Закрыть']")
    
    
    AUDIENCE_CREATE_SUBSCRIBERS = (By.XPATH, f"//*[contains(@class, 'ModalSidebarPage_container') and contains(div/h2, 'Подписчики сообществ')]//*[@data-testid='submit']")
    