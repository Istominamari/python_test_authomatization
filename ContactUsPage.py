from BasePage import BasePage
from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    NAME_INPUT = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    EMAIL_INPUT = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    CONTENT_TEXTAREA = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    SUBMIT_BUTTON = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/contact"

    def enter_name(self, name):
        field = self.find_element(ContactUsPageLocators.NAME_INPUT)
        field.clear()
        field.send_keys(name)

    def enter_email(self, email):
        field = self.find_element(ContactUsPageLocators.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)

    def enter_content(self, content):
        field = self.find_element(ContactUsPageLocators.CONTENT_TEXTAREA)
        field.clear()
        field.send_keys(content)

    def click_submit_button(self):
        self.find_element(ContactUsPageLocators.SUBMIT_BUTTON).click()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text
