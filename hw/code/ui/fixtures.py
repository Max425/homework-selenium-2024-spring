import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from hw.code.ui.pages.registration_page import RegistrationPage
from ui.pages.cases_page import CasesPage
from ui.pages.home_page import HomePage
from ui.pages.budget_page import BudgetPage
from ui.pages.main_page import MainPage
from dotenv import load_dotenv
from ui.pages.auth_page import AuthPage

LOGIN_URL = 'https://ads.vk.com/hq/registration'

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
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


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
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


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def cases_page(driver):
    driver.get(CasesPage.url)
    return CasesPage(driver=driver)

@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)

@pytest.fixture
def registration_page(driver):
    driver.get(LOGIN_URL)
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
def budget_page(driver, home_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)
