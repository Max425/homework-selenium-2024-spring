from ui.pages.home_page import HomePage
from selenium.common import TimeoutException
from ui.locators.education_locators import EducationLocators
from selenium.webdriver.support import expected_conditions as EC


class EducationPage(HomePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = EducationLocators()

    def open_education_modal(self):
        self.click(self.locators.TRAINING_BUTTON)

    def education_modal_visible(self):
        return self.is_visible(self.locators.EDUCATION_MODAL)

    def education_modal_not_visible(self):
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
