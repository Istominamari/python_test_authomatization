from BasePage import BasePage


class PostsListPage(BasePage):
    def get_user_menu_text(self):
        return self.get_text_from_element("USER_MENU_LINK")

    def click_create_post_button(self):
        self.click_on_element("GOTO_CREATE_POST_BUTTON")

    def click_to_contact_us_link(self):
        self.click_on_element("GOTO_CONTACT_US_LINK")
