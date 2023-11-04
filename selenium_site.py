import time
import yaml
from selenium.webdriver import FirefoxOptions, Firefox, ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.safe_load(f)


class Site:
    def __init__(self, address):
        browser = config["selenium_browser"]
        if browser == 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = FirefoxOptions()
            self.driver = Firefox(service=service, options=options)
        elif browser == 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = ChromeOptions()
            self.driver = Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(config["selenium_sleep_time"])

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, css_property):
        element = self.find_element(mode, path)
        if element is not None:
            return element.value_of_css_property(css_property)
        else:
            return None

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
