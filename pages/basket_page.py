import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_not_product_in_basket(self):
        # проверка что товаров в корзине нет
        print("should_not_product_in_basket")
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Success product is in basket ,but should not be"

    def should_be_see_text_about_basket_empty(self):
        # проверка что текст о том что корзина пуста есть
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), \
            "Text: basket is empty, is not presented"

    def is_element_present(self, how, what):
        # проверка элемент должен быть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # элемент не появляется на странице в течение заданного времени timeout=4
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            print("try is not el pre")
        except TimeoutException:
            print("false is not el pre")
            return True
        print("false is disap")
        return False
