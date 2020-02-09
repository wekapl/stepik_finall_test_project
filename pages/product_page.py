import time

import self as self
from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    #def should_be_can_add_product_to_basket(self):
    #    self.should_be_message_about_product_in_basket()
    #    self.should_be_name_product_as_baskets_name_product()
    #    self.should_be_message_about_price()
    #    self.shout_be_price_products_as_baskets_price()

    def should_be_message_about_product_in_basket(self):
        # сообщение о добавлении продукта в корзину
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "No message add product to basket is not presented"

    def should_be_name_product_as_baskets_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print('название продукта: ' + name_product)
        # print('стоимость продукта в корзине: ' + self.browser.find_element(
        # *ProductPageLocators.MESSAGE_PRODUCT_PRICE).text)
        name_product_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        print('название продукта: в сообщении: ' + name_product_basket)
        assert name_product_basket == name_product, \
            "Name product not as name product in basket"

    def should_be_message_about_price(self):
        # сообщение о стоимости продукта в корзине
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), \
            "No message add product to basket is not presented"

    def shout_be_price_products_as_baskets_price(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print('стоимость продукта: ' + price_product)
        # print('стоимость продукта в корзине: ' + self.browser.find_element(
        # *ProductPageLocators.MESSAGE_PRODUCT_PRICE).text)
        price_product_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        print('стоимость продукта в сообщении: ' + price_product_basket)
        assert price_product_basket == price_product, \
            "Price product not as price product in basket"

    def add_product_in_basket(self):
        print('название продукта(добавляем в корзину): ' + self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text)
        print('стоимость продукта(добавляем в корзину): ' + self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text)
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

        self.solve_quiz_and_get_code()

    def should_be_button_add_product_in_basket(self):
        # проверка что кнопка есть
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "Button add product to basket is not presented"
