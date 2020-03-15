from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASS1 = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASS2 = (By.XPATH, "//input[@name='registration-password2']")


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    MESSAGE_PRODUCT_NAME = (By.XPATH, '//div[@class="alertinner "]/strong')
    MESSAGE_PRODUCT_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    TEXT_BASKET_EMPTY = (By.XPATH, '//div[@id="content_inner"]')
    PRODUCTS_IN_BASKET = (By.CLASS_NAME, 'basket-items')
    BASKET_LINK = (By.CLASS_NAME, 'btn-group')
