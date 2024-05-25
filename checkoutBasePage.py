import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.checkoutPage import loginPage, checkoutPage

def test_tc037_validBillingAddress(self, emailInput, passInput, firstNameInput, lastNameInput, emailBillingInput, countryInput, stateInput, cityInput, addressInput, zipInput, phoneInput, message):
    # Define browser and access to Login URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Login Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()

    # Go to the checkout page
    browser.get(checkoutPage.checkout_url)

    # Get the field element
    first_name_field = browser.find_element(By.NAME, checkoutPage.first_name_field)
    last_name_field = browser.find_element(By.NAME, checkoutPage.last_name_field)
    email_field = browser.find_element(By.NAME, checkoutPage.email_field)

    # Assert that the email field is not empty and contains the expected email
    assert first_name_field.get_attribute("value") != "", "First name field is empty"
    assert first_name_field.get_attribute("value") == firstNameInput, f"First name field does not contain expected value {firstNameInput}"
    assert last_name_field.get_attribute("value") != "", "Last name field is empty"
    assert last_name_field.get_attribute("value") == lastNameInput, f"Last name field does not contain expected value {lastNameInput}"
    assert email_field.get_attribute("value") != "", "Email is required."
    assert email_field.get_attribute("value") == emailInput, f"Email field does not contain expected email {emailInput}"

    # Print a log message to show the value of the email field
    print(f"First name field contains: {first_name_field.get_attribute('value')}")
    print(f"Last name field contains: {last_name_field.get_attribute('value')}")
    print(f"Email field contains: {email_field.get_attribute('value')}")

    browser.quit()

def test_tc038_emptyFields(self, emailInput, passInput, msgCountry, msgCity, msgAddress, msgZip, msgPhone):
    # Define browser and access to Login URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Login Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()

    # Go to the checkout page
    browser.get(checkoutPage.checkout_url)

    # # Select the country field and select the first option
    # country_field = Select(browser.find_element(By.NAME, checkoutPage.country_field))
    # country_field.select_by_value(0)

    # # Select the state field and select the first option
    # state_field = Select(browser.find_element(By.NAME, checkoutPage.state_field))
    # state_field.select_by_value(0)

    # Finding the continue button and click it
    browser.find_element(By.XPATH, checkoutPage.continue_btn).click()

    # Get the error message elements
    empty_country = browser.find_element(By.CSS_SELECTOR, checkoutPage.err_country_field).text
    empty_city = browser.find_element(By.CSS_SELECTOR, checkoutPage.err_city_field).text
    empty_address = browser.find_element(By.CSS_SELECTOR, checkoutPage.err_address_field).text
    empty_zip = browser.find_element(By.CSS_SELECTOR, checkoutPage.err_zip_field).text
    empty_phone = browser.find_element(By.CSS_SELECTOR, checkoutPage.err_phone_field).text

    # Validation
    self.assertIn(msgCountry, empty_country)
    self.assertIn(msgCity, empty_city)
    self.assertIn(msgAddress, empty_address)
    self.assertIn(msgZip, empty_zip)
    self.assertIn(msgPhone, empty_phone)

    browser.quit()