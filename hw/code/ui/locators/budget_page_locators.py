from selenium.webdriver.common.by import By


class BudgetPageLocators:
    REPLENISH_BUDGET_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Пополнить счёт']")
    REPLENISHMENT_MODAL = (By.ID, "_modal_17")

    CLOSE_MODAL_PAGE_BUTTON = (By.XPATH, "//*[@aria-label='Закрыть']")

    AMOUNT_INPUT = (By.NAME, "amount")
    AMOUNT_WITHOUT_VAT_INPUT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")

    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")
    
    VKPAY_IFRAME = (By.CSS_SELECTOR, "iframe.CreateInvoiceModal_iframe #Main")