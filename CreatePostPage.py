from BasePage import BasePage
from selenium.webdriver.common.by import By


class CreatePostPageLocators:
    TITLE_INPUT = (By.XPATH, """// * [ @ id="create-item"] / div / div / div[1] / div / label / input""")
    DESCRIPTION_TEXTAREA = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    CONTENT_TEXTAREA = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    CREATE_POST_BUTTON = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")


class CreatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = f"{self.base_url}/posts/create"

    def enter_title(self, title):
        title_input = self.find_element(CreatePostPageLocators.TITLE_INPUT)
        title_input.clear()
        title_input.send_keys(title)

    def enter_description(self, description):
        description_textarea = self.find_element(CreatePostPageLocators.DESCRIPTION_TEXTAREA)
        description_textarea.clear()
        description_textarea.send_keys(description)

    def enter_content(self, content):
        content_textarea = self.find_element(CreatePostPageLocators.CONTENT_TEXTAREA)
        content_textarea.clear()
        content_textarea.send_keys(content)

    def click_create_button(self):
        self.find_element(CreatePostPageLocators.CREATE_POST_BUTTON).click()
