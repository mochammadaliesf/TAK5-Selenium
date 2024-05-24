import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginPage import loginData
import loginBasePage

class authLoginTest(unittest.TestCase):
    # Define chrome as a webdriver
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    # Inserting test data to each test cases
    # Insert test data for TC014
    def test_tc014_successLogin(self):
        loginBasePage.test_tc014_successLogin(
            self,
            loginData.valid_email,
            loginData.valid_password,
            loginData.msg_success_login)
    
    # Insert test data for TC017
    def test_tc017_invalidEmail(self):
        loginBasePage.test_tc017_invalidEmail(
            self,
            loginData.invalid_email,
            loginData.valid_password,
            loginData.msg_unregistered_email)
        
    # Insert test data for TC019
    def test_tc019_wrongEmail(self):
        loginBasePage.test_tc019_wrongEmail(
            self,
            loginData.invalid_email,
            loginData.wrong_pass,
            loginData.msg_wrong_pass)


if __name__ == '__main__':
    unittest.main()