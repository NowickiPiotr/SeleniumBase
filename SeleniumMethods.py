from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumMethods():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, value, timing):
        try:
            WebDriverWait(self.driver, timing).until(EC.element_to_be_clickable((value)))
        except:
            print("time out")

    def element_click(self, value, element, timing):
        try:
            WebDriverWait(self.driver, timing).until(EC.element_to_be_clickable((value)))
        except:
            print("time out")
        element.click()

    def is_displayed(self, locator,value):
        return self.driver.find_element(locator, value).is_displayed()

    # todo: rebuild
    # def element_on_list_click(self,value, element, element_index,timing):
    #     try:
    #         WebDriverWait(self.driver, timing).until(EC.element_to_be_clickable((value)))
    #     except:
    #         print("time out")
    #     element[element_index].click()
