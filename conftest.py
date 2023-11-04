import pytest
import yaml
from rest import login
from selenium_site import Site

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


@pytest.fixture
def incorrect_word():
    return "Малоко"


@pytest.fixture
def correct_word():
    return "Молоко"


@pytest.fixture
def rest_login():
    return login(config["username"], config["password"])


@pytest.fixture
def rest_title():
    return "White cat"


@pytest.fixture
def post_data():
    return "Как я провела лето.", "Рассказ о том, как я провела летние каникулы.", "Нормально."


@pytest.fixture
def selenium_site():
    site = Site(config["selenium_address"])
    yield site
    site.quit()


@pytest.fixture
def locators():
    return {
        "login_input": """//*[@id="login"]/div[1]/label/input""",
        "password_input": """//*[@id="login"]/div[2]/label/input""",
        "login_button": "button",
        "error_message": """//*[@id="app"]/main/div/div/div[2]/h2""",
        "user_menu": """//*[@id="app"]/main/nav/ul/li[3]/a""",
        "to_create_post_button": """//*[@id="create-btn"]""",
        "post_title_input": """// * [ @ id="create-item"] / div / div / div[1] / div / label / input""",
        "post_description_textarea": """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""",
        "post_content_textarea": """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""",
        "create_post_button": """//*[@id="create-item"]/div/div/div[7]/div/button""",
        "new_post_title": """//*[@id="app"]/main/div/div[1]/h1"""
    }


@pytest.fixture
def login_fail_data():
    return {
        "login": "test",
        "password": "test",
        "error_number": "401",
    }


@pytest.fixture
def login_success_data():
    return {
        "login": config["username"],
        "password": config["password"],
    }
