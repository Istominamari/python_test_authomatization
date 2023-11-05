from BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    PASSWORD_INPUT = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button")
    ERROR_MESSAGE = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/login"

    def enter_login(self, login):
        login_input = self.find_element(LoginPageLocators.LOGIN_INPUT)
        login_input.clear()
        login_input.send_keys(login)

    def enter_password(self, password):
        pass_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)

    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_text(self):
        error_message = self.find_element(LoginPageLocators.ERROR_MESSAGE)
        return error_message.text
