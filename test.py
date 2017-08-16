from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from Seat_Capacity import  SeatCapacity
from SeleniumMethods import SeleniumMethods

class ORM_SWR(unittest.TestCase):

    def setUp(self):
        self.geckoPath = "C:\\Python33\\BrowersDriver\\geckodriver\\geckodriver.exe"
        self.chromePath = "C:\\Python33\\BrowersDriver\\chromedriver\\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chromePath)
        self.driver.get("http://demo.test.southwesternrailway.com/travel-updates/seat-capacity")
        self.my_selenium_method = SeleniumMethods(self.driver)

    def tearDown(self):
        pass
        #self.driver.quit()

    def test_title_of_seat_capacity(self):
        self.assertEqual(self.driver.title,"Seat capacity")


    def test_learn_seat(self):
        self.driver.execute_script("window.scrollTo(0, 1600)")
        self.my_selenium_method.click(*SeatCapacity.later_services_button)
        #element = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CLASS_NAME, "icon-right_arrow"))
        #)
        #driver.find_element_by_xpath(".//*[@id='seat-availability-results']/div[2]/div/div[3]/div[4]/span/span").click()
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #element = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CLASS_NAME, "icon-left_arrow"))
        #)
        #driver.find_element_by_class_name("icon-left_arrow").click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ORM_SWR)
    unittest.TextTestRunner(verbosity=2).run(suite)









