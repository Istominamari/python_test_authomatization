import logging
import pytest

from ContactUsPage import ContactUsPage
from CreatePostPage import CreatePostPage
from LoginPage import LoginPage
from PostsListPage import PostsListPage
from ViewPostPage import ViewPostPage


class TestSelenium:

    def test_login_fail(self, browser, login_fail_data, login_fail_error_code):
        logging.info("Start test \"test_login_fail\".")
        page = LoginPage(browser)
        page.go_to_site()
        page.enter_login(login_fail_data[0])
        page.enter_password(login_fail_data[1])
        page.click_login_button()
        page.sleep()
        assert page.get_error_text() == login_fail_error_code

    def test_login_success(self, browser, login_success_data):
        logging.info("Start test \"test_login_success starting\".")
        login_page = LoginPage(browser)
        login_page.go_to_site()

        login_page.enter_login(login_success_data[0])
        login_page.enter_password(login_success_data[1])
        login_page.click_login_button()
        login_page.sleep()

        posts_list_page = PostsListPage(browser)
        assert posts_list_page.get_user_menu_text() == f'Hello, {login_success_data[0]}'

    def test_publish_post(self, browser, post_data):
        logging.info("Start test \"test_publish_post\".")
        posts_list_page = PostsListPage(browser)
        posts_list_page.go_to_site()
        posts_list_page.click_create_post_button()
        posts_list_page.sleep()

        create_post_page = CreatePostPage(browser)
        create_post_page.enter_title(post_data[0])
        create_post_page.enter_description(post_data[1])
        create_post_page.enter_content(post_data[2])
        create_post_page.click_create_button()
        create_post_page.sleep()

        view_post_page = ViewPostPage(browser)
        assert view_post_page.get_post_title() == post_data[0]

    def test_contact_us_form_sending(self, browser, contact_us_data, contact_us_alert_text):
        logging.info("Start test \"test_contact_us_form_sending\".")
        posts_list_page = PostsListPage(browser)
        posts_list_page.go_to_site()
        posts_list_page.click_to_contact_us_link()
        posts_list_page.sleep()

        contact_us_page = ContactUsPage(browser)
        contact_us_page.enter_name(contact_us_data[0])
        contact_us_page.enter_email(contact_us_data[1])
        contact_us_page.enter_content(contact_us_data[2])
        contact_us_page.click_submit_button()
        contact_us_page.sleep()
        assert contact_us_page.get_alert_text() == contact_us_alert_text


if __name__ == '__main__':
    pytest.main(["-v"])
