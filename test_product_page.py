import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

from .pages.main_page import MainPage


@pytest.mark.parametrize('link', ["0"])
# , "1", "2", "3", "4", "5", "6",
# pytest.param("7", marks=pytest.mark.xfail(reason="test fail")),
# "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
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


@pytest.mark.xfail(reason="test fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_be_disappearance_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
