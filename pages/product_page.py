from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_can_add_product_to_basket(self):
        self.should_be_massage_about_product_in_basket()
        self.should_be_massages_name_product_as_baskets_name_product()
        self.should_be_massage_about_price()
        self.shout_be_price_products_as_baskets_price()

    # def should_be_massage_about_product_in_basket(self):

    #######

    # def should_be_massages_name_product_as_baskets_name_product(self):
    #######

    # def should_be_massage_about_price(self):
    ########

    # def shout_be_price_products_as_baskets_price(self):
    ######

    def add_product_in_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_button_add_product_in_basket(self):
        # проверка что кнопка есть
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "Button add product to basket is not presented"
