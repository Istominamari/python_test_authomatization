from BasePage import BasePage


class CreatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/posts/create"

    def enter_title(self, title):
        self.enter_text_into_field("TITLE_INPUT", title)

    def enter_description(self, description):
        self.enter_text_into_field("DESCRIPTION_TEXTAREA", description)

    def enter_content(self, content):
        self.enter_text_into_field("POST_CONTENT_TEXTAREA", content)

    def click_create_button(self):
        self.click_on_element("CREATE_POST_BUTTON")
