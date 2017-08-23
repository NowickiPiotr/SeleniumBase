from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from Seat_Capacity import  SeatCapacity
from SeleniumMethods import SeleniumMethods


class AppManagerConfig():
    def __init__(self):
        self.geckoPath = "C:\\Python33\\BrowersDriver\\geckodriver\\geckodriver.exe"
        self.chromePath = "C:\\Python33\\BrowersDriver\\chromedriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromePath)
        self.url = "http://demo.test.southwesternrailway.com/travel-updates/seat-capacity"

class AppManager():
    def __init__(self, config):
        self._config = config

        self.driver = self._config.driver
        self.driver.get(self._config.url)
        self.driver.maximize_window()

        self._start_page = None

    def config(self):
        return self._config

    def closeWeb(self):
        self.driver.quit()

    @property
    def startPage(self):
        if self._start_page is None:
            self._start_page = FirstPage(self.driver)
        return self._start_page

class FirstPage():
    def __init__(self, driver):
        self.driver = driver
        self._later_services_button = None
        self._search_button = None

        self.my_selenium_method = SeleniumMethods(self.driver)
        self.seat_capacity_page=SeatCapacity()



    @property
    def later_services_button(self):
        if self._later_services_button is None:
            self._later_services_button =self.driver.find_element(*SeatCapacity.later_services_button_xpath)
        return  self._later_services_button

    def later_services_button_click(self):
        #self.later_services_button.click()
        self.my_selenium_method.element_click(self.seat_capacity_page.later_services_button_xpath,
                                              self.later_services_button,
                                              120)

    @property
    def search_button(self):
        if self._search_button is None:
            self._search_button = self.driver.find_element(*SeatCapacity.search_sevices_button)
        return self._search_button


    def search_button_click(self):
        self.my_selenium_method.element_click(self.seat_capacity_page.search_sevices_button,
                                              self.search_button,
                                              120)


    #
# app_config = AppManagerConfig()
# app_manager = AppManager(app_config)
# start_page = app_manager.startPage
# first = FirstPage(start_page)
# first.search_button_click()

