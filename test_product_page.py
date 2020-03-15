import time

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # функция, которая выполнится перед запуском каждого теста из класса
        # регистрируемся с новым пользователем и проверяем что он залогинен
        login_link = f"http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        product_page = LoginPage(browser, login_link)
        product_page.open()
        # почта и пароль для регистрации
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + email
        product_page.register_new_user(email, password)
        product_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # тест для гостя нет сообщения об успехе
        product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # тест гость может добавить продукт в корзину
        # есть конпка, добавляем товар в корзину, сообщение о добавлении(названия совподают)
        # сообщение о цене(цены совпадают)
        product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
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


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6",
                                  pytest.param("7", marks=pytest.mark.xfail(reason="test fail")),
                                  "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    # тест с параментром url - для товара из промо акции -  7 тест падает
    # тест пользователь может добавить продукт в корзину
    # есть конпка, добавляем товар в корзину, сообщение о добавлении(названия совподают)
    # сообщение о цене(цены совпадают)
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
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
    # тест нет сообщения об успехе после добавления товара в корзину - тест падает
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # тест для пользователя нет сообщения об успехе
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # тест нет сообщения об успехе после добавления товара в корзину - тест падает
    product_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    print(product_link)
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_in_basket()
    product_page.should_be_disappearance_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # тест должна быть ссылка на страницу логина на странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # тест переход на страницу логина со странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # тест в корзина пуста - переход на страницу корзины со страницы товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = BasketPage(browser, link)
    # открываем страницу
    page.open()
    page.go_to_basket_page()
    page.should_be_not_product_in_basket()
    page.should_be_see_text_about_basket_empty()
