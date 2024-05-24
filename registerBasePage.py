# Importing necessary modules and libraries
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.registerPage import registerPage

# Test case 001 (Success register with valid data)
def test_tc001_successRegister(self, firstNameInput, lastNameInput, emailInput, passInput, confirmPassInput, message):
    # Define browser and access to register URL
    browser = self.browser
    browser.get(registerPage.register_url)
    self.assertIn('Register', self.browser.title)

    # Inserting the keys to each field on the Register Page
    gender = browser.find_element(By.ID, "gender-male")
    gender.click()

    browser.find_element(By.ID, registerPage.first_name).send_keys(firstNameInput)
    browser.find_element(By.ID, registerPage.last_name).send_keys(lastNameInput)
    browser.find_element(By.ID, registerPage.email_field).send_keys(emailInput)
    browser.find_element(By.ID, registerPage.pass_field).send_keys(passInput)
    browser.find_element(By.ID, registerPage.confirm_pass_field).send_keys(confirmPassInput)
    # Finding a button attribut and click it
    browser.find_element(By.ID, registerPage.register_btn).click()
    # Finding the success register attribute
    success_register = browser.find_element(By.XPATH, registerPage.success_register_msg).text
    # Test validation
    self.assertIn(message, success_register)
    browser.quit()

# Test case 007 (Register with an existing data)
def test_tc007_existsRegister(self, firstNameInput, lastNameInput, emailInput, passInput, confirmPassInput, message):
    # Define browser and access to register URL
    browser = self.browser
    browser.get(registerPage.register_url)
    self.assertIn('Register', self.browser.title)

    # Inserting the keys to each field on the Register Page
    gender = browser.find_element(By.ID, "gender-male")
    gender.click()

    browser.find_element(By.ID, registerPage.first_name).send_keys(firstNameInput)
    browser.find_element(By.ID, registerPage.last_name).send_keys(lastNameInput)
    browser.find_element(By.ID, registerPage.email_field).send_keys(emailInput)
    browser.find_element(By.ID, registerPage.pass_field).send_keys(passInput)
    browser.find_element(By.ID, registerPage.confirm_pass_field).send_keys(confirmPassInput)
    # Finding a button attribut and click 
    browser.find_element(By.ID, registerPage.register_btn).click()
    # Finding the success register attribute
    exists_register = browser.find_element(By.XPATH, registerPage.exists_register_msg).text
    # Test validation
    self.assertIn(message, exists_register)
    browser.quit()

# Test case 008 (Register with unmatch password)
def test_tc008_unmatchPassword(self, firstNameInput, lastNameInput, emailInput, passInput, confirmPassInput, message):
    # Define browser and access to register URL
    browser = self.browser
    browser.get(registerPage.register_url)
    self.assertIn('Register', self.browser.title)

    # Inserting the keys to each field on the Register Page
    gender = browser.find_element(By.ID, "gender-male")
    gender.click()

    browser.find_element(By.ID, registerPage.first_name).send_keys(firstNameInput)
    browser.find_element(By.ID, registerPage.last_name).send_keys(lastNameInput)
    browser.find_element(By.ID, registerPage.email_field).send_keys(emailInput)
    browser.find_element(By.ID, registerPage.pass_field).send_keys(passInput)
    browser.find_element(By.ID, registerPage.confirm_pass_field).send_keys(confirmPassInput)
    # Finding a button attribut and click 
    browser.find_element(By.ID, registerPage.register_btn).click()
    # Finding the success register attribute
    unmatch_password = browser.find_element(By.CSS_SELECTOR, registerPage.unmatch_password_msg).text
    # Test validation
    self.assertIn(message, unmatch_password)
    browser.quit()

# Test case 009 (Register with empty first name)
def test_tc009_emptyFirstName(self, firstNameInput, lastNameInput, emailInput, passInput, confirmPassInput, message):
    # Define browser and access to register URL
    browser = self.browser
    browser.get(registerPage.register_url)
    self.assertIn('Register', self.browser.title)

    # Inserting the keys to each field on the Register Page
    gender = browser.find_element(By.ID, "gender-male")
    gender.click()

    browser.find_element(By.ID, registerPage.first_name).send_keys(firstNameInput)
    browser.find_element(By.ID, registerPage.last_name).send_keys(lastNameInput)
    browser.find_element(By.ID, registerPage.email_field).send_keys(emailInput)
    browser.find_element(By.ID, registerPage.pass_field).send_keys(passInput)
    browser.find_element(By.ID, registerPage.confirm_pass_field).send_keys(confirmPassInput)
    # Finding a button attribut and click 
    browser.find_element(By.ID, registerPage.register_btn).click()
    # Finding the success register attribute
    empty_first_name = browser.find_element(By.CSS_SELECTOR, registerPage.empty_name_register_msg).text
    # Test validation
    self.assertIn(message, empty_first_name)
    browser.quit()