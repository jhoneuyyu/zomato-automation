from pages.sign_page import Sign_Page



def test_signin_zomato(driver):
    """
    Tests the signin functionality of the Zomato website.

    """

    signin=Sign_Page(driver)
    signin.open_site()
    signin.click_sign_button()
    signin.enter_full_name("Venkateshwar Shavi")
    signin.enter_email("vshavi060@gmail.com")
    signin.click_box()
    signin.cre_acc_btn()

