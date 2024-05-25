import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageObject.cartPage import loginPage, cartPage

# Test case tc024 (Checkout success)
def test_tc024_checkoutSuccess(self, emailInput, passInput, itemQty, message):
    # Define browser and access to Login URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Login Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()

    # go to the cart page
    browser.get(cartPage.cart_url)

    # Inserting the keys to each field on the Cart Page
    check_item = browser.find_element(By.NAME, cartPage.check_item)
    check_item.click()
    # Insert the qty of item = 1
    browser.find_element(By.NAME, cartPage.qty_item).send_keys(itemQty)

    # Checking the ToS checkbox
    check_tos = browser.find_element(By.NAME, cartPage.check_tos)
    check_tos.click()

    browser.find_element(By.NAME, cartPage.checkout_btn).click()

    checkout_success = browser.find_element(By.XPATH, cartPage.checkout_success).text
    self.assertEqual(message, checkout_success)
    browser.quit()

# Test case tc036 (Uncheck ToS)
def test_tc036_uncheckedTOS(self, emailInput, passInput, itemQty, message):
    # Define browser and access to Login URL
    browser = self.browser
    browser.get(loginPage.login_url)

    # Inserting the keys to each field on the Login Page
    browser.find_element(By.NAME, loginPage.email_field).send_keys(emailInput)
    browser.find_element(By.NAME, loginPage.pass_field).send_keys(passInput)
    # Finding the login button and click it
    browser.find_element(By.CLASS_NAME, loginPage.login_btn).click()

    # go to the cart page
    browser.get(cartPage.cart_url)

    # Inserting the keys to each field on the Cart Page
    check_item = browser.find_element(By.NAME, cartPage.check_item)
    check_item.click()
    # Insert the qty of item = 1
    browser.find_element(By.NAME, cartPage.qty_item).send_keys(itemQty)

    # Checking the ToS checkbox
    # check_tos = browser.find_element(By.NAME, cartPage.check_tos)
    # check_tos.click()

    browser.find_element(By.NAME, cartPage.checkout_btn).click()

    unchecked_tos = browser.find_element(By.ID, cartPage.checkout_fail).text
    self.assertEqual(message, unchecked_tos)
    browser.quit()

