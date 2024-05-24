import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.registerPage import registerData
import registerBasePage

class authRegisterTest(unittest.TestCase):
    # Define chrome as a webdriver
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    # Inserting test data to each test cases
    # Insert test data for TC001
    def test_tc001_successRegister(self):
        registerBasePage.test_tc001_successRegister(
            self, 
            registerData.valid_first_name,
            registerData.valid_last_name,
            registerData.valid_email,
            registerData.valid_password,
            registerData.valid_password,
            registerData.msg_register_success)
    
    # Insert test data for TC007
    def test_tc007_existsRegister(self):
        registerBasePage.test_tc007_existsRegister(
            self, 
            registerData.valid_first_name,
            registerData.valid_last_name,
            registerData.valid_email,
            registerData.valid_password,
            registerData.valid_password,
            registerData.msg_register_exists)
    
    # Insert test data for TC008
    def test_tc008_unmatchPassword(self):
        registerBasePage.test_tc008_unmatchPassword(
            self, 
            registerData.valid_first_name,
            registerData.valid_last_name,
            registerData.valid_email,
            registerData.valid_password,
            registerData.unmatch_confirm_password,
            registerData.msg_unmatch_password)
        
    # Insert test data for TC009
    def test_tc009_emptyFirstName(self):
        registerBasePage.test_tc009_emptyFirstName(
            self, 
            registerData.empty_first_name,
            registerData.valid_last_name,
            registerData.valid_email,
            registerData.valid_password,
            registerData.valid_password,
            registerData.msg_empty_first_name)
    
if __name__ == '__main__':
    unittest.main()