import time

import pytest
import yaml

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


def login(selenium_site, locators, login_data):
    input1 = selenium_site.find_element("xpath", locators["login_input"])
    input1.send_keys(login_data["login"])
    input2 = selenium_site.find_element("xpath", locators["password_input"])
    input2.send_keys(login_data["password"])
    btn = selenium_site.find_element("css", locators["login_button"])
    btn.click()
    time.sleep(config["selenium_sleep_time"])


class TestSelenium:

    def test_login_fail(self, selenium_site, locators, login_fail_data):
        login(selenium_site, locators, login_fail_data)
        err_label = selenium_site.find_element("xpath", locators["error_message"])
        assert err_label.text == login_fail_data["error_number"]

    def test_login_success(self, selenium_site, locators, login_success_data):
        login(selenium_site, locators, login_success_data)
        user_menu = selenium_site.find_element("xpath", locators["user_menu"])
        assert user_menu.text == f'Hello, {login_success_data["login"]}'

    def test_publish_post(self, selenium_site, locators, login_success_data, post_data):
        login(selenium_site, locators, login_success_data)
        to_create_btn = selenium_site.find_element("xpath", locators["to_create_post_button"])
        to_create_btn.click()
        time.sleep(config["selenium_sleep_time"])

        title_input = selenium_site.find_element("xpath", locators["post_title_input"])
        title_input.send_keys(post_data[0])
        description_textarea = selenium_site.find_element("xpath", locators["post_description_textarea"])
        description_textarea.send_keys(post_data[1])
        content_textarea = selenium_site.find_element("xpath", locators["post_content_textarea"])
        content_textarea.send_keys(post_data[2])
        create_btn = selenium_site.find_element("xpath", locators["create_post_button"])
        create_btn.click()
        time.sleep(config["selenium_sleep_time"])

        new_post_title = selenium_site.find_element("xpath", locators["new_post_title"])
        assert new_post_title.text == post_data[0]


if __name__ == '__main__':
    pytest.main(["-v"])
