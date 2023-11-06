import logging
import time
import yaml
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


class Locators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.sleep_time = config["selenium_sleep_time"]
        self.base_url = config["selenium_base_url"]
        self.driver.maximize_window()

    def sleep(self):
        logging.debug(f"Sleep for {self.sleep_time}s.")
        time.sleep(self.sleep_time)

    def go_to_site(self):
        logging.debug(f"Go to {self.base_url}")
        try:
            start_browsing = self.driver.get(self.base_url)
            self.sleep()
        except:
            logging.exception("Exception while open site.")
            start_browsing = None
        return start_browsing

    def find_element(self, locator, timeout=10):
        logging.debug(f"Search element \"{locator}\".")
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                                message=f"Can't find element by locator \"{locator}\".")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, css_property):
        logging.debug(f"Getting \"{css_property}\" css-property of element \"{locator}\".")
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(css_property)
        else:
            logging.error(f"Property {property} not found in element with locator \"{locator}\".")
            return None

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert.")
            return None

    def enter_text_into_field(self, locator, text):
        logging.debug(f"Send \"{text}\" to element \"{locator}\".")
        field = self.find_element(Locators.ids.get(locator))
        if not field:
            logging.error(f"Element {locator} not found.")
            return False
        try:
            field.clear()
            field.send_keys(text)
        except:
            logging.exception(f"Exception while operate with \"{locator}\".")
            return False
        return True

    def get_text_from_element(self, locator):
        field = self.find_element(Locators.ids.get(locator))
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from \"{locator}\".")
            return None
        logging.debug(f"Whe find text \"{text}\" in field \"{locator}\".")
        return text

    def click_on_element(self, locator):
        element = self.find_element(Locators.ids.get((locator)))
        if not element:
            return False
        try:
            element.click()
        except:
            logging.exception(f"Exception with click on \"{locator}\".")
            return False
        logging.debug(f"Clicked on \"{locator}\".")
        return True
