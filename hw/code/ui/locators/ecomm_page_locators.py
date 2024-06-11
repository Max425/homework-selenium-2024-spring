from selenium.webdriver.common.by import By


class EcommPageLocators:
    CREATE_CATALOG_COMMON_BUTTON = (By.XPATH, f"//*[@data-testid='create-catalog']")
    CANCEL_EDUCATION = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Не сейчас']")
    MODAL_EDUCATION = (By.XPATH, "//*[contains(@class, 'vkui__portal-root')]")

    MODAL_OF_NEW_CATALOG = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_container__Zopae')]")

    CATALOG_NAME_INPUT = (By.XPATH, f"//*[@data-testid='catalogName-input']")

    FEED_OR_COMUNITY = (By.XPATH, "//*[@data-entityid='url']")
    MARKETPLACE = (By.XPATH, "//*[@data-entityid='marketplace']")
    ADD_FILE = (By.XPATH, "//*[@data-entityid='file']")

    CATALOG_PAGE_HISTORY = (By.ID, "catalogs.catalogMain.catalogHistory")

    CREATE_CATALOG_FINISH_BUTTON = (By.XPATH, "//*[@data-testid='submit']")
    CANCEL_CATALOG_FINISH_BUTTON = (By.XPATH, f"//*[@data-testid='cancel']")

    URL_INPUT = (By.XPATH, "//*[@data-testid='catalogUrl-input']")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")
    ERROR_MESSAGE_BANNER = (By.XPATH, "//span[contains(@class, 'formBanner_text')]")

    ADD_API_KEY = (By.XPATH, "//*[@placeholder='Введите ключ API']")

    GOOD_DROPDOWN = (By.XPATH, "//*[@role='combobox']")
    GOOD_AUTO = (By.XPATH, "//*[@value='auto']")
    GOOD_EXAMPLE = (By.XPATH, f"//*[@target='_blank']")

    CATALOGS_TABLE = (By.XPATH, "//*[@role='table']")

    SPINNER_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiSpinner vkuiButton__spinner')]")

    ECOMM_MENU_BUTTON = (By.XPATH, "//*[contains(@href, '/hq/ecomm/catalogs')]")

    CATALOG_TITLE = (By.XPATH, "//*[contains(@class, 'CatalogNavigationCell')]")

    CATALOG_STATUS = (By.XPATH, "//*[contains(@class, 'StatusCell_cell')]")

    @staticmethod
    def PRODUCT_CARD(title):
        return (By.XPATH, f"//*[contains(@class, 'NameCell_itemNameBlock_') and contains(h5, '{title}')]")
    
    @staticmethod
    def BUTTON(lable):
        return (By.XPATH, f"//*[contains(@class, 'vkuiButton__in')]/span[text()='{lable}']")
    
    MODAL_CONFIRM_DELETE = (By.XPATH, "//div[contains(@class, 'ModalConfirm_wrapper')]")

    FILE_INPUT = (By.XPATH, "//input[@class='vkuiVisuallyHidden' and @type='file']")

    GROUPS_TAB = (By.ID, 'tab_catalogs.catalogMain.catalogGroups')

    CREATE_GROUP = (By.XPATH, "//*[contains(@class, 'CatalogGroups_controls')]/button")

    GROUP_DROPDOWN = (By.XPATH, "//*[contains(@class, 'CatalogGroups_createGroupDropdown__')]/div")

    CONDITION_INPUT = (By.XPATH, "//*[contains(@class, 'Condition_formItem')]//input[contains(@class, 'vkuiText') and @value='0']")

    GROUP_NAME_INPUT = (By.NAME, "groupName")

    @staticmethod
    def GROUP_HEADER(header):
        return (By.XPATH, f"//*[contains(@class, 'CatalogGroupHeader_header__') and contains(div, '{header}')]")
    
    PRODUCT_TITLE  = (By.XPATH, "//*[contains(@class, 'NameCell_itemNameBlock_')]/h5")

    CLOSE_EDUCATION_BUTTON = (By.XPATH, "//*[contains(@class, 'CloseButton_iconWrapper__')]")