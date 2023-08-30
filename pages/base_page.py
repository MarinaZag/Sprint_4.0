from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def start_page(self, page_url):
        self.driver.get(page_url)

    def find_element(self, element):
        return self.driver.find_element(*element)

    def find_wait_location_element(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(element))

    def element_not_displayed(self, element, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.presence_of_element_located(element))

    def add_value(self, element, value):
        self.find_element(element).send_keys(value)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(element))

    def click_element(self, element):
        self.find_element(element).click()

    def wait_element_click(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))

    def wait_visibility_element(self, element, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))

    def cross_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def find_text(self, element):
        return self.find_element(element).text

    def wait_url_to_be(self, page_url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(page_url))

    def find_elements_located(self, element, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(element))