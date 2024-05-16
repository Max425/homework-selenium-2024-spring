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

    MODAL_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'ModalRoot_componentWrapper')and .//h2[text()='Ключевые фразы']]//button[@type='submit']")
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
