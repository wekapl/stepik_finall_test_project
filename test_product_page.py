import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.main_page import MainPage


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail(reason="test fail")),
                                  "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_button_add_product_in_basket()
    product_page.add_product_in_basket()
    product_page.should_be_message_about_product_in_basket()
    product_page.should_be_message_about_price()
    product_page.should_be_name_product_as_baskets_name_product \
        (product_page.name_product_in_element(ProductPageLocators.PRODUCT_NAME))
    product_page.shout_be_price_products_as_baskets_price \
        (product_page.name_product_in_element(ProductPageLocators.PRODUCT_PRICE))
