from selenium.webdriver.common.by import By

class EcommPageLocators:
    CREATE_CATALOG_COMMON_BUTTON = (By.XPATH, "//*[contains(@class, 'Catalogs_toolbar__CWsCD')]/button[contains(@class, 'vkuiButton')]")
    CREATE_CATALOG_HEADER = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_header__kW4ug')]/h2[contains(@class, 'vkuiTypography vkuiTypography--normalize vkuiTypography--weight-2 ModalSidebarPage_title__Uu-FC vkuiTitle--level-2')]")
    MODAL_OF_NEW_CATALOG = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__uzHTL')]")
    
    CATALOG_NAME_INPUT = (By.XPATH, "//*[@data-test-id='catalogName-input']")
    CATALOG_NAME_HEADER = (By.XPATH, "//*[contains(@class, 'vkuiFormItem vkuiFormItem--withPadding vkuiInternalFormItem vkuiFormItem--sizeY-none vkuiInternalFormItem--sizeY-none vkuiFormItem--withTop vkuiInternalFormItem--withTop')]/span[contains(@class, 'FormItem_topText__cD8oZ')]")
    
    ADDING_POSITIONS_HEADER = (By.XPATH, "//*[contains(@class, 'vkuiFormItem vkuiFormItem--withPadding vkuiInternalFormItem vkuiFormItem--sizeY-none vkuiInternalFormItem--sizeY-none vkuiFormItem--withTop vkuiInternalFormItem--withTop')]/span[contains(@class, 'FormItem_topText__cD8oZ')]")
    
    FEED_OR_COMUNITY_HEADER = (By.XPATH, "//*[@data-entityid='url']/h4[contains(@class, 'vkuiTypography vkuiTypography--normalize vkuiTypography--weight-2 vkuiHeadline--sizeY-none vkuiHeadline--level-1')]")
    MARKETPLACE_HEADER = (By.XPATH, "//*[@data-entityid='marketplace']/h4[contains(@class, 'vkuiTypography vkuiTypography--normalize vkuiTypography--weight-2 vkuiHeadline--sizeY-none vkuiHeadline--level-1')]")
    ADD_FILE_HEADER = (By.XPATH, "//*[@data-entityid='file']/h4[contains(@class, 'vkuiTypography vkuiTypography--normalize vkuiTypography--weight-2 vkuiHeadline--sizeY-none vkuiHeadline--level-1')]")
    
    FEED_OR_COMUNITY = (By.XPATH, "//*[@data-entityid='url']")
    MARKETPLACE = (By.XPATH, "//*[@data-entityid='marketplace']")
    ADD_FILE = (By.XPATH, "//*[@data-entityid='file']")

    CREATE_CATALOG_FINISH_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton vkuiButton--size-l vkuiButton--mode-primary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--sizeY-none vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible')]/span[contains(@class, 'vkuiButton__content')]")
    CANCEL_CATALOG_FINISH_BUTTON = (By.XPATH, "//button[contains(@class, 'vkuiButton vkuiButton--size-l vkuiButton--mode-secondary vkuiButton--appearance-accent vkuiButton--align-center vkuiButton--sizeY-none vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible')]/span[contains(@class, 'vkuiButton__content')]")
    
    FEED_URL_INPUT = (By.XPATH, "//*[@data-test-id='catalogUrl-input']")    



