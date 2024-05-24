import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.loginPage import loginPage

# Test case tc014 (Success login)
def test_tc014_successLogin(self, emailInput, passInput, message):
     # Define browser and access to register URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Login Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()
    # Finding the success register attribute
    success_login = browser.find_element(By.CSS_SELECTOR, loginPage.success_login_msg).text
    # Test validation
    self.assertIn(message, success_login)
    browser.quit()

# Test case tc017 (Unregistered email)
def test_tc017_invalidEmail(self, emailInput, passInput, message):
     # Define browser and access to register URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Register Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()
    # Finding the success register attribute
    invalid_email = browser.find_element(By.XPATH, loginPage.unregistered_email_msg).text
    # Test validation
    self.assertIn(message, invalid_email)
    browser.quit()

# Test case tc019 (Wrong password)
def test_tc019_wrongEmail(self, emailInput, passInput, message):
     # Define browser and access to register URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Register Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()
    # Finding the success register attribute
    wrong_pass = browser.find_element(By.CSS_SELECTOR, loginPage.wrong_pass_msg).text
    # Test validation
    self.assertIn(message, wrong_pass)
    browser.quit()