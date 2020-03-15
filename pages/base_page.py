import math
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, BasketPageLocators


class BasePage:

    def __init__(self, browser: RemoteWebDriver, url):
        # конструктор
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(30)

    def open(self):
        # открывает страницу в браузере, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # проверка элемент должен быть на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # элемент не появляется на странице в течение заданного времени timeout=4
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            print("try is not el pre")
        except TimeoutException:
            print("false is not el pre")
            return True
        print("false is disap")
        return False

    def is_disappeared(self, how, what, timeout=4):
        # элемент исчезает в течение заданного времени timeout=4
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
            print("try is disap")
        except TimeoutException:
            print("false is disap")
            return False
        print("true is disap")
        return True

    def solve_quiz_and_get_code(self):
        # капча
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        # переход на страницу регистрации
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        # переход в корзину
        button_basket = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        button_basket.click()

    def should_be_login_link(self):
        # проверка что ссылка на страницу регистрации есть
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def should_be_authorized_user(self):
        # проверка что пользователь залогинен
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
