from selenium.webdriver.common.by import By


class CompanyPageLocators:
    SKIP_HELP_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Попробовать позже']")
    CREATE_COMPANY_BUTTON = (
        By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать']")
    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Продолжить']")

    SITE = (By.XPATH, "//*[@data-id='site_conversions']")
    SITE_INPUT = (By.XPATH, "//*[@placeholder='Введите ссылку на сайт']")

    ERROR = (By.XPATH, "//*[@role='alert']/div")

    GOAL_DROPDOWN = (By.XPATH, "//*[@data-testid='priced-goal']")
    STRATEGY_DROPDOWN = (By.XPATH, "//*[@data-testid='autobidding-mode']")
    BUDGET_INPUT = (By.XPATH, "//*[contains(@class, 'Budget_input__')]/input")

    DATES = (By.XPATH, "//*[contains(@class, 'Dates_layout__')]")
    START_DATE = (By.XPATH, "//*[contains(@class, 'Dates_datepickerStart__')]/input")


    NEURO_IMAGE = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and child::div/div[text()='Созданное нейросетью']]")
    NEURO_IMAGE_FOR_MEDIA = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Созданное нейросетью']")
    ADD_IMAGE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить (1/7)']")
    IMAGE = (By.XPATH, "//*[@id='media-library-image']/div/div/div[1]/div[1]")
    PUBLIC_COMPANY = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Опубликовать']")

    @staticmethod
    def ACTIVE_STAGE(stage_name):
        return By.XPATH, f"//*[contains(@class, 'Steps_step_active__') and child::span[text()='{stage_name}']]"

    REGION_QUICK_SELECTION = (By.XPATH, "//*[contains(@class, 'RegionsQuickSelection_item__')]")

    MEDIA_BUTTON = (By.XPATH, "//*[contains(@class, 'UploadMediaButton_buttonLogoTitle__') and text()='Выбрать логотип']")
    PANEL_TITLE = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_title')]")
    GENERATED_IMAGES_TAB = (By.ID, "tab-media-library-photobank")
    IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ImageItems_image__')]")
    SELECTED_IMAGE = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_loaded__')]")

    TITLE = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//input")
    DESCRIPTION = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//textarea")

    PREVIEW_TITLE = (By.XPATH, "//*[contains(@class, 'preview_preview__')]//h3[contains(@class, 'Header_name__')]")
    PREVIEW_DESCRIPTION = (
        By.XPATH, "//*[contains(@class, 'preview_preview__')]//*[contains(@class, 'Default_text__')]")

    PUBLISH_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Опубликовать']")
