from ui.pages.home_page import HomePage
from selenium.common import TimeoutException
from ui.locators.education_locators import EducationLocators
from selenium.webdriver.support import expected_conditions as EC


class EducationPage(HomePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = EducationLocators()

    def open_education_modal(self):
        self.click(self.locators.TRAINING_BUTTON)

    def is_education_modal_visible(self):
        return self.is_visible(self.locators.EDUCATION_MODAL)

    def is_education_modal_not_visible(self):
        return self.is_invisible(self.locators.EDUCATION_MODAL)

    def is_two_windows(self):
        try:
            self.wait().until(EC.number_of_windows_to_be(2))
            return True
        except TimeoutException:
            return False

    def title_is(self, title):
        try:
            self.wait().until(EC.title_is(title))
            return True
        except TimeoutException:
            return False
    
    def is_education_item_visible(self, item):
        return self.is_visible(self.locators.EDUCATION_ITEM(item))
    
    def is_later_button_visible(self):
        return self.is_visible(self.locators.LATER_BUTTON)
    
    def click_close_modal_button(self):
        self.click(self.locators.CLOSE_MODAL_BUTTON)

    def click_later_button(self):
        self.click(self.locators.LATER_BUTTON)

    def is_vk_public_modal_visible(self):
        return self.is_visible(self.locators.VK_PUBLIC_MODAL)
    
    def is_education_course_item_visible(self, item):
        return self.is_visible(self.locators.EDUCATION_COURSE_ITEM(item))
    
    def click_education_course_item(self, item):
        self.click(self.locators.EDUCATION_COURSE_ITEM(item))
    
    def is_videoplayer_visible(self):
        return self.is_visible(self.locators.VIDEO_PLAYER, timeout=5)

    def click_education_item(self, item):
        self.click(self.locators.EDUCATION_ITEM(item))



