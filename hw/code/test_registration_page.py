import pytest

from base_case import BaseCase


@pytest.fixture
def new_cabinet(registration_page):
    registration_page.click_create_new_cabinet_button()


class TestRegistrationPage(BaseCase):
    def test_open_use_cabinet_myTarget(self, registration_page):
        registration_page.click_use_cabinet_myTarget_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/import/target')

    def test_open_new_cabinet_registration(self, registration_page):
        registration_page.click_create_new_cabinet_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/new')

    def test_change_account_type(self, registration_page, registration_new_page):
        registration_page.change_account_type('Агенство')
        assert self.is_opened('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')