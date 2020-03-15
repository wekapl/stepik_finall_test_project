from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        # тест что гость может перейти на страницу логина
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        # открываем страницу
        page.open()
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # тест что есть ссылка на страницу логина
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


# @pytest.mark.skip
def test_guest_should_see_login_page(browser):
    # тест что пользователь на странице логина
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_page()
    page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # тест что пользователь переходит в конзину, корзина пуста
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = BasketPage(browser, link)
    # открываем страницу
    page.open()
    time.sleep(5)
    page.go_to_basket_page()
    time.sleep(5)
    page.should_be_not_product_in_basket()
    page.should_be_see_text_about_basket_empty()
