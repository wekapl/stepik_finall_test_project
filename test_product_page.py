from .pages.product_page import ProductPage
from .pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_button_add_product_in_basket()
    product_page.add_product_in_basket()
    product_page.should_be_message_about_product_in_basket()
    product_page.should_be_name_product_as_baskets_name_product()
    product_page.should_be_message_about_price()
    product_page.shout_be_price_products_as_baskets_price()