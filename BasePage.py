import logging
import time
import yaml
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.sleep_time = config["selenium_sleep_time"]
        self.base_url = config["selenium_base_url"]
        self.driver.maximize_window()

    def sleep(self):
        logging.info(f"Sleep for {self.sleep_time}")
        time.sleep(self.sleep_time)

    def go_to_site(self):
        logging.info(f"Go to {self.base_url}")
        self.driver.get(self.base_url)
        self.sleep()

    def find_element(self, locator, timeout=10):
        logging.info(f"Search element {locator}")
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, css_property):
        logging.info(f"Getting \"{css_property}\" css-property of element {locator}")
        element = self.find_element(locator)
        if element is not None:
            return element.value_of_css_property(css_property)
        else:
            logging.warning(f"Element {locator} not exists!")
            return None
