import pytest
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.ecomm_page import EcommPage
from base_case import BaseCase
from ui.fixtures import driver
import time


@pytest.fixture
def create_new_catalog(ecomm_page):
    ecomm_page.cancel_education()
    WebDriverWait(driver, timeout=1).until(lambda d: ecomm_page.is_education_modal_closed())
    ecomm_page.create_new_catalog()

@pytest.fixture
def feed_or_comunity_catalog(ecomm_page, create_new_catalog):
    ecomm_page.add_position_feed_or_comunity()

@pytest.fixture
def file_upload_catalog(ecomm_page, create_new_catalog):
    ecomm_page.add_position_add_file()


class TestEcommPage(BaseCase):


    def test_comunity_catalog(self, ecomm_page : EcommPage, feed_or_comunity_catalog):
        # test_сreate
        ecomm_page.enter_catalog_name("Кислинка")
        ecomm_page.enter_url('https://vk.com/ksnlkkslnk')
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.is_catalog_page_opened()
        ecomm_page.open_ecomm()
        assert ecomm_page.is_catalogue_in_table("Товары – Кислинка")
        WebDriverWait(driver, timeout=60).until(lambda l: ecomm_page.is_catalogue_active("Товары – Кислинка"))
        ecomm_page.open_catalog("Товары – Кислинка")
        assert ecomm_page.is_catalog_table_created()
        assert ecomm_page.is_product_in_table("флиска с котюнчиком")

        #test_rename
        ecomm_page.open_settings()
        ecomm_page.enter_catalog_name("Кислые Товары")
        ecomm_page.finish_creating_catalog()
        ecomm_page.open_ecomm()
        assert not ecomm_page.is_catalogue_in_table("Товары – Кислинка")
        assert ecomm_page.is_catalogue_in_table("Кислые Товары")

        # test_delete
        ecomm_page.open_catalog("Кислые Товары")
        ecomm_page.open_settings()
        ecomm_page.click_delele_catalog()
        assert ecomm_page.is_confirm_delete_visible()
        ecomm_page.confirm_delete()
        WebDriverWait(driver, timeout=10).until(lambda l: ecomm_page.is_confirm_delete_invisible())
        assert not ecomm_page.is_catalogue_in_table("Кислые Товары")

    def test_community_catalog_no_products(self, ecomm_page : EcommPage, feed_or_comunity_catalog):
        ecomm_page.enter_url("https://vk.com/ga6a_pshod")
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.get_error_banner_text() == 'В этом сообществе недостаточно товаров или услуг'

    def test_create_file_upload_catalog(self, ecomm_page : EcommPage, file_upload_catalog):
        ecomm_page.enter_catalog_name('Каталог из файла')
        ecomm_page.upload_file("test_data/test_products.csv")
        ecomm_page.finish_creating_catalog()
        assert ecomm_page.is_catalog_page_opened()
        ecomm_page.open_ecomm()
        assert ecomm_page.is_catalogue_in_table("Каталог из файла")
        WebDriverWait(driver, timeout=100).until(lambda l: ecomm_page.is_catalogue_active("Каталог из файла"))
        ecomm_page.open_catalog("Каталог из файла")
        assert ecomm_page.is_product_in_table("Худи VK")

        ecomm_page.open_settings()
        ecomm_page.click_delele_catalog()
        ecomm_page.confirm_delete()
        WebDriverWait(driver, timeout=10).until(lambda l: ecomm_page.is_confirm_delete_invisible())

    def test_create_group(self, ecomm_page : EcommPage):
        ecomm_page.enter_catalog_name("Кислинка")
        ecomm_page.enter_url('https://vk.com/ksnlkkslnk')
        ecomm_page.finish_creating_catalog()
        ecomm_page.open_ecomm()
        WebDriverWait(driver, timeout=60).until(lambda l: ecomm_page.is_catalogue_active("Товары – Кислинка"))
        ecomm_page.open_catalog("Товары – Кислинка")


        ecomm_page.open_groups()
        ecomm_page.create_filter_group()
        ecomm_page.set_price_higher_than(3000)
        ecomm_page.set_group_name("Дорогие вещи")
        ecomm_page.finish_creating_catalog()
        ecomm_page.open_group("Дорогие вещи")
        product_titles = ecomm_page.get_products_titles()
        assert {"черные ультраштаны", "жилетка с котюнчиками", "флиска с котюнчиком"} == set(product_titles)

        ecomm_page.open_settings()
        ecomm_page.click_delele_catalog()
        ecomm_page.confirm_delete()
        WebDriverWait(driver, timeout=10).until(lambda l: ecomm_page.is_confirm_delete_invisible())



