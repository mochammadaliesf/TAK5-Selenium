# Login part
class loginPage():
    # Initiate attribute name on the login page
    login_url = 'https://demowebshop.tricentis.com/login'
    email_field = 'Email' #by name
    pass_field = 'Password' #by name
    login_btn = 'login-button' #by class name

class loginData():
    # Test data for log in
    login_url = 'https://demowebshop.tricentis.com/login'
    valid_email = 'ahmad.udin18@gmail.com'
    valid_password = 'Adun@1234'

# Cart part
# class cartPage():
#     # Initiate attribute name on the register page (By.NAME)
#     cart_url = 'https://demowebshop.tricentis.com/cart'
#     check_item = 'removefromcart'
#     qty_item = 'itemquantity4274720'
#     check_tos = 'termsofservice'
#     checkout_btn = 'checkout'

#     # Initiate responses attribute
#     checkout_fail = 'terms-of-service-warning-box'
#     checkout_success = '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]//h1[.="Checkout"]'      #By XPATH

# class cartData():
#     # Test data for tc024 (Success to checkout)
#     qty_item = '1'

#     # Message responses for each scenarios
#     msg_checkout_fail = 'Please accept the terms of service before the next step.'
#     msg_checkout_success = 'Checkout'

# Checkout part
class checkoutPage():
    # Initiate attribute name on the login page (By NAME)
    checkout_url = 'https://demowebshop.tricentis.com/onepagecheckout'
    first_name_field = 'BillingNewAddress.FirstName'
    last_name_field = 'BillingNewAddress.LastName'
    email_field = 'BillingNewAddress.Email'
    # By NAME
    country_field = 'BillingNewAddress.CountryId'
    state_field = 'BillingNewAddress.StateProvinceId'
    city_field = 'BillingNewAddress.City'
    address_field = 'BillingNewAddress.Address1'
    zip_field = 'BillingNewAddress.ZipPostalCode'
    phone_number_field = 'BillingNewAddress.PhoneNumber'

    continue_btn = '//div[@id="billing-buttons-container"]/input[@title="Continue"]'        #By XPATH
    err_email_field = '[data-valmsg-for="BillingNewAddress.Email"]'
    err_country_field = '[data-valmsg-for="BillingNewAddress.CountryId"]'
    err_city_field = '[data-valmsg-for="BillingNewAddress.City"]'
    err_address_field = '[data-valmsg-for="BillingNewAddress.Address1"]'
    err_zip_field = '[data-valmsg-for="BillingNewAddress.ZipPostalCode"]'
    err_phone_field = '[data-valmsg-for="BillingNewAddress.PhoneNumber"]'

class checkoutData():
    first_name = 'Ahmad'
    last_name = 'Udin'
    email = 'ahmad.udin18@gmail.com'
    country = ''
    state = ''
    city = ''
    address = ''
    zip = ''
    phone = ''

    msg_country = 'Country is required.'
    msg_city = 'City is required.'
    msg_address = 'Street address is required'
    msg_zip = 'Zip / postal code is required'
    msg_phone = 'Phone is required.'