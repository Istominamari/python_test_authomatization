from BasePage import BasePage


class ViewPostPage(BasePage):
    def get_post_title(self):
        return self.get_text_from_element("POST_TITLE")
