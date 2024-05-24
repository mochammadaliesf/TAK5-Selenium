import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.cartPage import loginData, cartData, cartPage
import cartBasePage

class cartToCheckout(unittest.TestCase):
    # Define chrome as a webdriver
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    # Inserting test data to each test cases
    # Insert test data for TC024
    def test_tc024_checkoutSuccess(self):
        cartBasePage.test_tc024_checkoutSuccess(
            self,
            loginData.valid_email,
            loginData.valid_password,
            cartData.qty_item,
            cartPage.checkout_success
        )

if __name__ == '__main__':
    unittest.main()