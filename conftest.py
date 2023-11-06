import pytest
import yaml
from rest import login
from selenium.webdriver import FirefoxOptions, Firefox, ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from send_report import send_report

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
    return "ПРО КОТА"


@pytest.fixture
def post_data():
    return "Как я провела лето.", "Рассказ о том, как я провела летние каникулы.", "Нормально."


@pytest.fixture(scope='session')
def browser():
    browser = config["selenium_browser"]
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = FirefoxOptions()
        driver = Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = ChromeOptions()
        driver = Chrome(service=service, options=options)
    driver.implicitly_wait(config["selenium_implicitly_wait"])
    yield driver
    driver.quit()


@pytest.fixture
def login_fail_data():
    return "test", "test"


@pytest.fixture
def login_fail_error_code():
    return "401"


@pytest.fixture
def login_success_data():
    return config["username"], config["password"]


@pytest.fixture
def contact_us_data():
    return config["username"], "test@test.test", "Test test test"


@pytest.fixture
def contact_us_alert_text():
    return "Form successfully submitted"


def pytest_unconfigure():
    send_report()
