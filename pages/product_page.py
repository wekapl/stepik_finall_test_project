import time

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def should_be_can_add_product_to_basket(self):
    #    self.should_be_message_about_product_in_basket()
    #    self.should_be_name_product_as_baskets_name_product()
    #    self.should_be_message_about_price()
    #    self.shout_be_price_products_as_baskets_price()

    def should_be_message_about_product_in_basket(self):
        # сообщение о добавлении продукта в корзину
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_NAME), \
            "No message add product to basket is not presented"

    def should_be_message_about_price(self):
        # сообщение о стоимости продукта в корзине
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_PRICE), \
            "No message add product to basket is not presented"

    def name_product_in_element(self, product_locator):
        # поиск элемента по локатору, возвращает текст_элемента
        name = self.browser.find_element(*product_locator).text
        print('название продукта: ' + name)
        return name

    def should_be_name_product_as_baskets_name_product(self, name):
        # совпадает ли название продукта с продуктом в корзине
        message_name = self.name_product_in_element(ProductPageLocators.MESSAGE_PRODUCT_NAME)
        assert name == message_name, \
            name + " product not as " + message_name + "product in basket"

    def shout_be_price_products_as_baskets_price(self, price):
        # совпадает ли цена продукта с ценой продукта в корзине
        message_price = self.name_product_in_element(ProductPageLocators.MESSAGE_PRODUCT_PRICE)
        assert price == message_price, \
            price + " product not as " + message_price + "product in basket"

    def add_product_in_basket(self):
        #  добавляем товар в корзину
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

        self.solve_quiz_and_get_code()

    def should_be_button_add_product_in_basket(self):
        # проверка что кнопка есть
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "Button add product to basket is not presented"