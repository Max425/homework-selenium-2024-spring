from selenium.webdriver.common.by import By


class CasesPageLocators:
    PAGE_TITLE = (By.XPATH, "//*[@data-test-id='summary-title-ads']")
    CASE_ITEM = (By.XPATH, "//a[contains(@class, 'Case_wrapper__')]")
    CASE_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title__')]")