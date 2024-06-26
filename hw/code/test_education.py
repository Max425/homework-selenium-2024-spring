import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_case import BaseCase


@pytest.fixture
def open_education_modal(education_page):
    education_page.open_education_modal()


@pytest.fixture
def vk_public(open_education_modal, education_page):
    education_page.click_education_item("Сообщество ВКонтакте")


class TestEducation(BaseCase):
    def test_education_modal_opens(self, open_education_modal, education_page):
        assert education_page.is_education_modal_visible()
        for item in ["Сообщество ВКонтакте", "Сайт", "Каталог товаров", "Мобильное приложение",
                     "Лид-формы", "VK Mini Apps", "Музыка", "Видео и трансляции", "Дзен"]:
            assert education_page.is_education_item_visible(item)
            
        assert education_page.is_later_button_visible()

    def test_education_modal_closes_on_button(self, open_education_modal, education_page):
        education_page.click_close_modal_button()
        assert education_page.is_education_modal_not_visible()

    def test_education_modal_closes_on_later_button(self, open_education_modal, education_page):
        education_page.click_later_button()
        assert education_page.is_education_modal_not_visible()

    def test_education_vk_public(self, vk_public, education_page):
        education_page.is_vk_public_modal_visible()
        for item in ["Настроить кампанию с подсказками", "Смотреть видеоурок от экспертов VK",
                     "Смотреть курс на обучающей платформе"]:
            assert education_page.is_education_course_item_visible(item)

    def test_education_vk_public_videolesson(self, vk_public, education_page):
        education_page.click_education_course_item("Смотреть видеоурок от экспертов VK")
        assert education_page.is_videoplayer_visible()

    def test_education_vk_public_learning_platform(self, vk_public, education_page):
        original_window = self.driver.current_window_handle
        education_page.click_education_course_item("Смотреть курс на обучающей платформе")
        education_page.wait().until(EC.number_of_windows_to_be(2))

        assert education_page.is_two_windows()

        for window_handle in education_page.driver.window_handles:
            if window_handle != original_window:
                education_page.driver.switch_to.window(window_handle)
                break

        assert education_page.title_is("Как продвигать сообщество в VK Рекламе — курс от Обучающей платформы VK")
