from datetime import datetime
import pytest
from base_case import BaseCase

SITE_URL = 'https://example.com'
TITLE = 'Подарок к празднику!'
DESCRIPTION = 'К Новому году подарим яркие и качественные подарки! В наличии на сайте. Успейте купить.'
BUDGET = 100

@pytest.fixture
def new_company(company_page):
    company_page.skip_help()
    company_page.click_create_company()


@pytest.fixture
def enter_site(new_company, company_page):
    company_page.select_site()
    company_page.enter_site_url(SITE_URL)


@pytest.fixture
def second_stage(enter_site, company_page):
    company_page.enter_budget_amount(BUDGET)
    company_page.click_continue_button()


@pytest.fixture
def third_stage(second_stage, company_page):
    company_page.select_regions()
    company_page.click_continue_button()


class TestCampaignsPage(BaseCase):

    def test_site_input_is_visible(self, new_company, company_page):
        company_page.select_site()
        assert company_page.site_input_is_visible()

    def test_additional_options_is_visible(self, enter_site, company_page):
        assert company_page.options_is_visible()

    def test_check_date(self, enter_site, company_page):
        assert company_page.get_start_date() == datetime.now().strftime('%d.%m.%Y')

    def test_open_second_stage(self, second_stage, company_page):
        assert company_page.is_active_stage(company_page.SECOND_STAGE_NAME)

    def test_open_third_stage(self, third_stage, company_page):
        assert company_page.is_active_stage(company_page.THIRD_STAGE_NAME)

    def test_open_media_browser(self, third_stage, company_page):
        company_page.click_media_button()
        assert company_page.get_panel_title() == 'Медиатека'

    def test_check_preview(self, third_stage, company_page):
        company_page.enter_title_and_description(TITLE, DESCRIPTION)
        assert company_page.get_preview_title() == TITLE
        assert company_page.get_preview_description() == DESCRIPTION
