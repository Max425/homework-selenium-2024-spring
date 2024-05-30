from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    url = 'https://ads.vk.com/'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_until(self, method, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout).until(method)

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=None):
        elem = self.find(locator, timeout=timeout)
        elem.click()

    def scroll_and_click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        return elem

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])

    def is_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element(locator))
            return True
        except TimeoutException:
            return False

    def fill_field(self, field, value):
        elem = self.find(field)
        elem.clear()
        elem.send_keys(value)

    def hover_elem(self, locator):
        elem = self.find(locator)
        ActionChains(self.driver).move_to_element(elem).perform()
