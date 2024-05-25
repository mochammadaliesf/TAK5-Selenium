import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.checkoutPage import loginData, checkoutData
import checkoutBasePage

class checkoutValidation(unittest.TestCase):
    # Define chrome as a webdriver
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Inserting test data to each test cases
    def test_tc37_validBillingAddress(self):
        checkoutBasePage.test_tc037_validBillingAddress(
            self,
            loginData.valid_email,
            loginData.valid_password,
            checkoutData.first_name,
            checkoutData.last_name,
            checkoutData.email,
            checkoutData.country,
            checkoutData.state,
            checkoutData.city,
            checkoutData.address,
            checkoutData.zip,
            checkoutData.phone,
            "Message"
        )
    
    # Inserting test data to each test cases
    def test_tc38_emptyFields(self):
        checkoutBasePage.test_tc038_emptyFields(
            self,
            loginData.valid_email,
            loginData.valid_password,
            checkoutData.country,
            checkoutData.city,
            checkoutData.address,
            checkoutData.zip,
            checkoutData.phone,
        )

if __name__ == "__main__":
    unittest.main()