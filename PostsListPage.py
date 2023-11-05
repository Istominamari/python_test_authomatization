from BasePage import BasePage
from selenium.webdriver.common.by import By


class PostsListPageLocators:
    USER_MENU = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    TO_CREATE_POST_BUTTON = (By.XPATH, """//*[@id="create-btn"]""")
    TO_CONTACT_US_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")


class PostsListPage(BasePage):
    def get_user_menu_text(self):
        user_menu = self.find_element(PostsListPageLocators.USER_MENU)
        return user_menu.text

    def click_create_post_button(self):
        to_create_post_button = self.find_element(PostsListPageLocators.TO_CREATE_POST_BUTTON)
        to_create_post_button.click()

    def click_to_contact_us_link(self):
        to_contact_us_link = self.find_element(PostsListPageLocators.TO_CONTACT_US_LINK)
        to_contact_us_link.click()
