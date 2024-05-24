class loginPage():
    # Initiate attribute name on the login page
    login_url = 'https://demowebshop.tricentis.com/login'
    email_field = 'Email' #by name
    pass_field = 'Password' #by name
    login_btn = 'login-button' #by class name

    # Initiate responses attribute on the login page
    success_login_msg = '.ico-logout'  #by CSS Selector
    unregistered_email_msg = '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]/div[@class="center-2"]//form[@action="/login"]//ul/li[.="No customer account found"]'  #by XPATH
    wrong_pass_msg = '.message-error'  #by Class

class loginData():
    # Test data for tc014 (Success login)
    login_url = 'https://demowebshop.tricentis.com/login'
    valid_email = 'ahmad.udin18@gmail.com'
    valid_password = 'Adun@1234'

    # Test data for tc017 (Unregistered email)
    invalid_email = 'ahmadudin212@gmail.com'

    # Test data for tc019 (Wrong password)
    wrong_pass = '1234asdf'

    # Message responses for each scenario
    msg_success_login = 'Log out'
    msg_unregistered_email = 'No customer account found'
    msg_wrong_pass = 'Login was unsuccessful. Please correct the errors and try again.\nNo customer account found'