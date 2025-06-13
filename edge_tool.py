from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import random
import time


def wait(low, high):
    t = random.randint(low, high)
    print("wait {} seconds......\n".format(t))
    time.sleep(t)
    return None


def retry(tries=3, delay=1, exceptions=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as E:
                    print(f"Retry {i+1} times after for {delay} seconds...")
                    time.sleep(delay)
            print("Executive failure...")
            return None
        return wrapper
    return decorator


class MyEdge:
    def __init__(self, driver_path):
        option = Options()
        # option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = driver_path
        self.browser = webdriver.Edge(service=Service(executable_path=driver), options=option)

    @retry()
    def get_url(self, url: str):
        self.browser.get(url)
        self.browser.maximize_window()
        #  ActionChains(self.browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform
        self.browser.execute_script("var q=document.documentElement.scrollTop=0")  # scroll up
        print("Successfully opened '{}'...".format(url))
        wait(1,2)
        return None

    @retry()
    def click_ele_by_xpath(self, xpath: str):
        self.browser.find_element(By.XPATH,xpath).click()
        print("Successfully click '{}'...".format(xpath))
        wait(1,2)
        return None

    @retry()
    def click_ele_by_id(self, id_value: str):
        self.browser.find_element(By.ID, id_value).click()
        print("Successfully click '{}'...".format(id_value))
        wait(1,2)
        return None

    @retry()
    def fill_ele_by_xpath(self, xpath: str, value: str):
        self.browser.find_element(By.XPATH, xpath).send_keys(value)
        print("Successfully fill '{}' with {}...".format(xpath, value))
        wait(1,2)
        return None

    @retry()
    def fill_ele_by_id(self, id_value: str, value: str):
        self.browser.find_element(By.ID, id_value).send_keys(value)
        print("Successfully fill '{}' with {}...".format(id_value, value))
        wait(1,2)
        return None

    def find_ele_by_xpath(self, xpath: str, times: int):
        result = False
        ele = None
        for _ in range(times):
            print(f'Search for {xpath} with {_ + 1} times...\n')
            try:
                ele = self.browser.find_element(By.XPATH, xpath)
                result = True
                print(f'Search successfully...\n')
                wait(1,2)
                break
            except NoSuchElementException:
                pass
        return result, ele

    def refresh(self):
        self.browser.refresh()
        print("Successfully refreshed the browser...")
        wait(1,2)
        return None

    def close(self):
        self.browser.close()
        self.browser.quit()
        print("Successfully closed the browser...")
        wait(1,2)
        return None

