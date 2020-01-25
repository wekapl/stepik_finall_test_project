from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы - переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def go_to_login_page(self):
    login_link = self.browser.find_element_by_css_selector("#login_link")
    login_link.click()
    alert = self.browser.switch_to.alert
    alert.accept()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    page.should_be_login_page()
    page.should_be_login_url()
