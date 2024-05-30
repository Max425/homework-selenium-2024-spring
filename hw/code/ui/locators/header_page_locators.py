from selenium.webdriver.common.by import By


class HeaderPageLocators:
    VK_LOGO_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiLink')]")

    CHANGE_ACCOUNT_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiIcon--w-12')]")

    ALL_CABINETS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/settings/access')]")

    WALLET_BUTTON = (By.XPATH, f"//*[contains(@class, 'balance_balance__epeyd')]")

    REPLENISH_WALLET_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton')]//span[text()='Пополнить счёт']")

    NOTIFICATIONS_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiIcon--notification_outline_24')]")

    NOTIFICATIONS_CONTENT = (By.XPATH, f"//*[contains(@class, 'vkuiHeader__main')]")

    USER_AVATAR_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiImageBase__img')]")

    QUIT_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiIcon--door_arrow_right_outline_20')]")
