from base_case import BaseCase


class TestBudgetPage(BaseCase):
    MIN_AMOUNT = 600
    MIN_AMOUNT_WITHOUT_VAT = 500
    CORRECT_AMOUNT = 800
    CORRECT_AMOUNT_WITH_VAT = 960
    RUBLE_END = " ₽"

    AMOUNT_FIELD_TITLE = "Cумма к оплате"
    AMOUNT_WITHOUT_VAT_FIELD_TITLE = "Сумма, поступающая на ваш счёт"
    VKPAY_IFRAME_TITLE = "Пополнение рекламного счета"

    ERROR_TOO_SMALL_AMOUNT = 'Минимальная сумма 600,00 ₽'

    def test_open_replenishment_modal_page(self, budget_page):
        budget_page.click_replenish_budget_button()
        assert budget_page.replenishment_modal_visible()
        assert self.AMOUNT_FIELD_TITLE in self.driver.page_source
        assert self.AMOUNT_WITHOUT_VAT_FIELD_TITLE in self.driver.page_source

    def test_correct_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(self.CORRECT_AMOUNT_WITH_VAT)
        assert str(self.CORRECT_AMOUNT) + self.RUBLE_END == budget_page.get_amount_without_vat_value()
        budget_page.click_submit_button()
        assert budget_page.vkpay_iframe_visible()
        # vkpay = budget_page.get_vkpay_iframe()
        # assert self.VKPAY_IFRAME_TITLE in vkpay.get_attribute('innerHTML')
        # assert str(self.CORRECT_AMOUNT_WITH_VAT) in vkpay.get_attribute('innerHTML')

    def test_correct_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat(self.CORRECT_AMOUNT)
        assert str(self.CORRECT_AMOUNT_WITH_VAT) + self.RUBLE_END == budget_page.get_amount_value()
        budget_page.click_submit_button()
        assert budget_page.vkpay_iframe_visible()
        # vkpay = budget_page.get_vkpay_iframe()
        # assert self.VKPAY_IFRAME_TITLE in vkpay.get_attribute('innerHTML')
        # assert str(self.CORRECT_AMOUNT_WITH_VAT) in vkpay.get_attribute('innerHTML')
        
    def test_error_too_small_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount(self.MIN_AMOUNT - 1)
        assert budget_page.get_error_message() == self.ERROR_TOO_SMALL_AMOUNT

    def test_error_too_small_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat(self.MIN_AMOUNT_WITHOUT_VAT - 1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == self.ERROR_TOO_SMALL_AMOUNT
