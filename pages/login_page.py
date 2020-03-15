from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        # проверка что перешли на страницу логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверку, что подстрока "login" есть в текущем url браузера
        assert "login" in str(self.browser.current_url), \
            "the login page did not open"
        assert True

    def should_be_login_form(self):
        #  проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"
        assert True

    def should_be_register_form(self):
        #  проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        # регистрируем нового пользователя
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS1)
        input_pass1.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS2)
        input_pass2.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_registration.click()

