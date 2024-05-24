class loginPage():
    # Initiate attribute name on the login page
    login_url = 'https://demowebshop.tricentis.com/login'
    email_field = 'Email' #by name
    pass_field = 'Password' #by name
    login_btn = 'login-button' #by class name

class cartPage():
    # Initiate attribute name on the register page (By.NAME)
    cart_url = 'https://demowebshop.tricentis.com/cart'
    check_item = 'removefromcart'
    qty_item = 'itemquantity4274720'
    check_tos = 'termsofservice'
    checkout_btn = 'checkout'

    # Initiate responses attribute
    checkout_fail = 'div#terms-of-service-warning-box > p'
    checkout_success = 'https://demowebshop.tricentis.com/onepagecheckout'

class loginData():
    # Test data for log in
    login_url = 'https://demowebshop.tricentis.com/login'
    valid_email = 'ahmad.udin18@gmail.com'
    valid_password = 'Adun@1234'

class cartData():
    # Test data for tc024 (Success to checkout)
    qty_item = '1'

    # Message responses for each scenarios
    msg_checkout_fail = 'Please accept the terms of service before the next step.'