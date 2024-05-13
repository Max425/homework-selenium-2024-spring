import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from hw.code.ui.pages.registration_page import RegistrationPage
from ui.pages.home_page import HomePage
from ui.pages.budget_page import BudgetPage
from ui.pages.main_page import MainPage
from ui.pages.audience_page import AudiencePage
from dotenv import load_dotenv
from ui.pages.auth_page import AuthPage
from ui.pages.money_page import MoneyPage
from ui.pages.menu_page import MenuPage
from ui.pages.header_page import HeaderPage
from ui.pages.forum_page import ForumPage
from ui.pages.settings_notifications_page import SettingsNotificationsPage

LOGIN_URL = 'https://ads.vk.com/hq/registration'


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    options.add_argument("window-size=1200x600")
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def money_page(driver):
    driver.get(MoneyPage.url)
    return MoneyPage(driver=driver)


@pytest.fixture
def forum_page(driver):
    driver.get(ForumPage.url)
    return ForumPage(driver=driver)


@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')


@pytest.fixture(scope='session')
def credentials_without_login():
    load_dotenv()
    return os.getenv('LOGIN_WITHOUT_CABINET'), os.getenv('PASSWORD_WITHOUT_CABINET')


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def registration_page(driver, credentials_without_login, auth_page):
    driver.get(LOGIN_URL)
    auth_page.login(*credentials_without_login)
    return RegistrationPage(driver=driver)


@pytest.fixture
def registration_new_page(registration_page):
    registration_page.click_create_new_cabinet_button()


@pytest.fixture
def home_page(driver, credentials, auth_page):
    driver.get(LOGIN_URL)
    auth_page.login(*credentials)
    return HomePage(driver=driver)


@pytest.fixture
def menu_page(driver, home_page):
    driver.get(MenuPage.url)
    return MenuPage(driver=driver)


@pytest.fixture
def header_page(driver, home_page):
    driver.get(HeaderPage.url)
    return HeaderPage(driver=driver)


@pytest.fixture
def settings_notifications_page(driver, home_page):
    driver.get(SettingsNotificationsPage.url)
    return SettingsNotificationsPage(driver=driver)


@pytest.fixture
def budget_page(driver, home_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)


@pytest.fixture
def audience_page(driver, home_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)
