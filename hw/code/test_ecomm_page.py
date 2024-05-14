import pytest
from base_case import BaseCase


@pytest.fixture
def replenishment_modal_page(ecomm_page):
    ecomm_page.create_new_catalog()


class TestEcommPage(BaseCase):

    def test_open_modal(self, replenishment_modal_page, ecomm_page):
        assert ecomm_page.new_catalog_modal_page_became_visible()

    def test_title_is_displayed(self, ecomm_page):
        assert ecomm_page.get_catalog_page_title() == 'Новый каталог'