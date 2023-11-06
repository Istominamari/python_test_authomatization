from BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/login"

    def enter_login(self, login):
        self.enter_text_into_field("LOGIN_INPUT", login)

    def enter_password(self, password):
        self.enter_text_into_field("PASSWORD_INPUT", password)

    def click_login_button(self):
        self.click_on_element("LOGIN_BUTTON")

    def get_error_text(self):
        return self.get_text_from_element("ERROR_MESSAGE")
