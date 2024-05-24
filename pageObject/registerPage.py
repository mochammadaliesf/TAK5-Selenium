class registerPage():
    # Initiate attribute name on the register page
    register_url = 'https://demowebshop.tricentis.com/register'
    first_name = 'FirstName'
    last_name = 'LastName'
    email_field = 'Email'
    pass_field = 'Password'
    confirm_pass_field = 'ConfirmPassword'
    register_btn = 'register-button'

    # Initiate responses attribute on the register page
    success_register_msg = '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]//div[@class="result"]'
    error_register_msg = '[class="field-validation-error"]'
    exists_register_msg = '//body/div[@class="master-wrapper-page"]/div[@class="master-wrapper-content"]/div[@class="master-wrapper-main"]//form[@action="/register"]//ul/li[.="The specified email already exists"]'
    empty_name_register_msg = '[data-valmsg-for="FirstName"]' 
    unmatch_password_msg = '[data-valmsg-for="ConfirmPassword"]'

class registerData():
    # Test data for TC001 & TC007
    register_url = 'https://demowebshop.tricentis.com/register'
    valid_first_name = 'Ahmad'
    valid_last_name = 'Udin'
    valid_email = 'ahmad.udin18@gmail.com'
    valid_password = 'Adun@1234'

    # Test data for TC008 (unmatch password)
    unmatch_confirm_password = 'Ahmad@1234'

    # Test data for TC009 (empty first name)
    empty_first_name = ''

    # Message reponses for each scenarios
    msg_register_success = 'Your registration completed'                                # Message for tc001
    msg_register_exists = 'The specified email already exists'                          # Message for tc007
    msg_empty_first_name = 'First name is required.'                                    # Message for tc009
    msg_unmatch_password = 'The password and confirmation password do not match.'       # Message for tc008

