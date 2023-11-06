from BasePage import BasePage


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/contact"

    def enter_name(self, name):
        self.enter_text_into_field("NAME_INPUT", name)

    def enter_email(self, email):
        self.enter_text_into_field("EMAIL_INPUT", email)

    def enter_content(self, content):
        self.enter_text_into_field("CONTACT_US_CONTENT_TEXTAREA", content)

    def click_submit_button(self):
        self.click_on_element("SUBMIT_BUTTON")
