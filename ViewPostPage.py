from BasePage import BasePage
from selenium.webdriver.common.by import By


class ViewPostPageLocators:
    POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")


class ViewPostPage(BasePage):
    def get_post_title(self):
        user_menu = self.find_element(ViewPostPageLocators.POST_TITLE)
        return user_menu.text
