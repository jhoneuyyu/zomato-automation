from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sign_Page:
    SIGNIN_BUTTON=(By.XPATH,"//a[.='Sign up']")
  
    FULL_NAME=(By.XPATH,"(//input[@type='text'])[1]")
    EMAIL=(By.XPATH,"(//input[@type='text'])[2]")
    CHECK_BOX=(By.XPATH,"//input[@class='sc-1o2pknd-1 iPRmnw']")
    CREATE_ACC=(By.XPATH,"(//span[@class='sc-1kx5g6g-2 eXneOi'])[2]")


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)
    
    def open_site(self):
        self.driver.get("https://www.zomato.com/bangalore/delivery")


    def click_sign_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SIGNIN_BUTTON)).click()
        except Exception as e:
            print(f"Error clicking login button: {e}") 


    

    def enter_full_name(self,fullname):
        try:
            self.wait.until(EC.visibility_of_element_located(self.FULL_NAME)).send_keys(fullname)

        except Exception as e:
            print(f"Error entering Full name: {e}")    



            
    def enter_email(self,mail):
        try:
            self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(mail)

        except Exception as e:
            print(f"Error in a  entering email: {e}")   


    def click_box(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX)).click()
        except Exception as e:
            print(f"Error in a click_box: {e}")  

    def cre_acc_btn(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CREATE_ACC)).click()
        except Exception as e:
            print(f"Error in a cre_acc_btn : {e}")          
