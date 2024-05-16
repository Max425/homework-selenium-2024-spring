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

    CREATE_CATALOG_FINISH_BUTTON = (By.XPATH, f"//*[@data-testid='submit']")
    CANCEL_CATALOG_FINISH_BUTTON = (By.XPATH, f"//*[@data-testid='cancel']")

    URL_INPUT = (By.XPATH, "//*[@data-testid='catalogUrl-input']")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")

    ADD_API_KEY = (By.XPATH, "//*[@placeholder='Введите ключ API']")

    GOOD_DROPDOWN = (By.XPATH, "//*[@role='combobox']")
    GOOD_AUTO = (By.XPATH, "//*[@value='auto']")
    GOOD_EXAMPLE = (By.XPATH, f"//*[@target='_blank']")

    CATALOGS_TABLE = (By.XPATH, "//*[@role='table']")

    SPINNER_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiSpinner vkuiButton__spinner')]")
