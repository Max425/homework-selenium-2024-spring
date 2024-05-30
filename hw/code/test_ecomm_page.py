import pytest
from selenium.webdriver.support.wait import WebDriverWait

from base_case import BaseCase
from ui.fixtures import driver


@pytest.fixture
def create_new_catalog(ecomm_page):
    ecomm_page.cancel_education()
    WebDriverWait(driver, timeout=1).until(lambda d: ecomm_page.is_education_modal_closed())
    ecomm_page.create_new_catalog()

@pytest.fixture
def feed_or_comunity_catalog(ecomm_page, create_new_catalog):
    ecomm_page.add_position_feed_or_comunity()


class TestEcommPage(BaseCase):
    wait = WebDriverWait(driver, timeout=1)

    # def test_open_modal(self, ecomm_page, create_new_catalog):
    #     assert ecomm_page.is_new_catalog_modal_page_became_visible()

    def test_comunity_catalog(self, ecomm_page, feed_or_comunity_catalog):
        ecomm_page.enter_catalog_name("Кислинка")
        ecomm_page.enter_url('https://vk.com/ksnlkkslnk')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.is_catalog_table_created()
        ecomm_page.open_ecomm()
        assert ecomm_page.is_catalogue_in_table("Товары – Кислинка")
        WebDriverWait(driver, timeout=60).until(lambda l: ecomm_page.is_catalogue_active())
        ecomm_page.open_catalog()
        assert ecomm_page.is_product_in_table("флиска с котюнчиком")
        ecomm_page.open_settings()
        ecomm_page.click_delele_catalog()
        assert ecomm_page.is_confirm_delete_visible()
        ecomm_page.confirm_delete()
        WebDriverWait(driver, timeout=60).until(lambda l: ecomm_page.is_confirm_delete_visible())
        assert not ecomm_page.is_catalogue_in_table("Товары – Кислинка")

        


