from selenium.webdriver.common.by import By


class MainPageLocators:
    CAMPAIGNS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/dashboard')]")

    AUDIENCE_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/audience')]")
    
    BUDGET_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/budget')]")
    
    TRAINING_BUTTON = (By.XPATH, f"//*[@data-testid='onboarding-button']")
    
    ECOMM_CATALOGS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/ecomm/catalogs')]")
    
    PIXELS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/pixels')]")
    
    APPS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/apps')]")
    
    LEADADS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/leadads')]")
    
    TRAINING_MODAL_CONTENT = (By.ID, "_modal_24")

    SETTINGS_BUTTON = (By.XPATH, f"//*[contains(@href, '/hq/settings')]")
