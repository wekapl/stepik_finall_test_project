from .pages.product_page import ProductPage
from .pages.main_page import MainPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    # добавить выполнение проверок добавление товара и сравнение цены
    #
    #
    
    product_page.add_product_in_basket()
    product_page.should_be_button_add_product_in_basket()


