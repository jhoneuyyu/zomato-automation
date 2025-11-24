from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Locators - use clear, consistent naming
    LOGIN_BUTTON = (By.XPATH, "//a[.='Log in']")
    PHONE_NUMBER = (By.XPATH, "//input[@type='number']")
    SEND_OTP_BUTTON = (By.XPATH, "(//span[.='Send One Time Password'])[2]")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//span[@class='sc-iGgWBj elhLRJ']")
    IFRAME = (By.XPATH, "//iframe[@id='auth-login-ui']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_site(self):
        self.driver.get("https://www.zomato.com/bangalore/delivery")

    def click_login_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        except Exception as e:
            print(f"Error clicking login button: {e}")

    def switch_to_login_iframe(self):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.IFRAME))
        except Exception as e:
            print(f"Error switching to iframe: {e}")

    def enter_phone_number(self, number):
        try:
            # Wait for element to be present AND visible
            phone_field = self.wait.until(
                EC.visibility_of_element_located(self.PHONE_NUMBER)
            )
            phone_field.clear()  # Clear any existing text
            phone_field.send_keys(number)
        except Exception as e:
            print(f"Error entering phone number: {e}")

    def click_send_otp(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SEND_OTP_BUTTON)).click()
        except Exception as e:
            print(f"Error clicking send OTP button: {e}")