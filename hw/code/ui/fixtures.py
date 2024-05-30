import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from ui.pages.audience_page import AudiencePage
from ui.pages.auth_page import AuthPage
from ui.pages.budget_page import BudgetPage
from ui.pages.ecomm_page import EcommPage
from ui.pages.education_page import EducationPage
from ui.pages.forum_page import ForumPage
from ui.pages.header_page import HeaderPage
from ui.pages.home_page import HomePage
from ui.pages.menu_page import MenuPage
from ui.pages.money_page import MoneyPage
from ui.pages.registration_page import RegistrationPage
from ui.pages.settings_access_page import SettingsAccessPage
from ui.pages.settings_common_page import SettingsCommonPage
from ui.pages.settings_history_page import SettingsHistoryPage
from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.pages.company_page import CompanyPage
from ui.pages.leadform_page import LeadformPage

LOGIN_URL = 'https://ads.vk.com/hq/registration'


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    if browser == 'chrome':
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
def settings_access_page(driver, home_page):
    driver.get(SettingsAccessPage.url)
    return SettingsAccessPage(driver=driver)


@pytest.fixture
def settings_history_page(driver, home_page):
    driver.get(SettingsHistoryPage.url)
    return SettingsHistoryPage(driver=driver)


@pytest.fixture
def budget_page(driver, home_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)


@pytest.fixture
def audience_page(driver, home_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)


@pytest.fixture
def education_page(driver, home_page):
    return EducationPage(driver=driver)


@pytest.fixture
def settings_common_page(driver, home_page):
    driver.get(SettingsCommonPage.url)
    return SettingsCommonPage(driver=driver)


@pytest.fixture
def ecomm_page(driver, home_page):
    driver.get(EcommPage.url)
    return EcommPage(driver=driver)

@pytest.fixture
def company_page(driver, home_page):
    driver.get(CompanyPage.url)
    return CompanyPage(driver=driver)

@pytest.fixture
def leadform_page(driver, home_page):
    driver.get(LeadformPage.url)
    return LeadformPage(driver=driver)