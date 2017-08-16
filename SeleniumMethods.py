from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumMethods(object):

    def __init__(self, driver):
        self.driver = driver

    def _find(self, locator,value):
        self.driver.find_element(locator,value)

    def is_displayed(self, locator,value):
        return self.driver.find_element(locator, value).is_displayed()

    def click(self,locator,value):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.element_to_be_clickable((locator, value)))
        self.driver.find_element(locator, value).click()

    def click_list(self,locator,value, element_index):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.element_to_be_clickable((locator, value)))
        self.driver.find_elements(locator, value)[element_index].click()

    def type_list_element(self, locator, value, input_text,element_index=0):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located((locator, value)))
        self.driver.find_elements(locator, value)[element_index].send_keys(input_text)
