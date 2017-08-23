from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
from Seat_Capacity import  SeatCapacity
from SeleniumMethods import SeleniumMethods
from AppManager import  AppManager, AppManagerConfig, FirstPage

class ORM_SWR(unittest.TestCase):

    def setUp(self):

        self.app_config = AppManagerConfig()
        self.app_manager = AppManager(self.app_config)
        self.start_page = self.app_manager.startPage

    def tearDown(self):
        self.app_manager.closeWeb()

    def test_check_content(self):
        assert self.start_page.later_services_button is not None
        assert self.start_page.search_button is not None

    def test_title_of_seat_capacity(self):
        self.assertEqual(self.app_manager.driver.title,"Seat capacity")

    def test_later_are_clickable(self):
        self.app_manager.driver.execute_script("window.scrollTo(0, 1600)")
        self.start_page.later_services_button_click()

    def test_search(self):
        self.start_page.search_button_click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ORM_SWR)
    unittest.TextTestRunner(verbosity=2).run(suite)









