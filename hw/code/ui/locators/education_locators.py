from selenium.webdriver.common.by import By


class EducationLocators:
    TRAINING_BUTTON = (By.XPATH, f"//*[@data-testid='onboarding-button']")

    EDUCATION_MODAL = (By.ID, "_modal_24")

    VK_PUBLIC_MODAL = (By.ID, "_modal_23")

    @staticmethod
    def EDUCATION_ITEM(label):
        return (By.XPATH, f"//*[contains(@class, 'Objects_item') and contains(div/div/div/span, '{label}')]")
    
    @staticmethod
    def EDUCATION_COURSE_ITEM(label):
        return (By.XPATH, f"//*[contains(@class, 'SelectObject_root') and contains(div, '{label}')]")
    
    LATER_BUTTON = (By.XPATH, "//*[contains(@class, 'Objects_closeModalButton__')]")

    CLOSE_MODAL_BUTTON = (By.XPATH, "//*[@aria-label='Закрыть']")

    VIDEO_PLAYER = (By.CSS_SELECTOR, ".videoplayer_media")
