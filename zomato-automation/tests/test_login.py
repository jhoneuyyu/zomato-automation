from pages.login_page import LoginPage


def test_login_zomato(driver):
    """
    Tests the login functionality of the Zomato website.
    """
    login = LoginPage(driver)
    login.open_site()
    login.click_login_button()
    login.switch_to_login_iframe()
    login.enter_phone_number('7019035690')
    login.click_send_otp()
    

   