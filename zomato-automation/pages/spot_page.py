from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep







class Bookspot:
    CLICK_TREND_SPOT=(By.XPATH,"(//div[@class='sc-bhlBdH csHSIR'])[1]")
    ENTER_LOCATION=(By.XPATH,"//input[@class='sc-jHZirH hAtUrG']")
    ENTER_PLACE_NAME=(By.XPATH,"(//input[@placeholder='Search for restaurant, cuisine or a dish'])[1]")
    CLICK_ON_SPOT=(By.XPATH,"(//div[@class='sc-1q7bklc-9 dYrjiw'][normalize-space()='DINING'])[1]")
    BOOK_TABLE=(By.XPATH,"(//div[@class='sc-emjYpo sc-vBKru krrQUS'])[2]")
    DATE_DROPDOWN = (By.XPATH, "(//div[@class='sc-qnejpk-11 kgudfR'])[1]")
    BOOKING_DATE=(By.XPATH,"(//div[@class='sc-10vdmo9-4 hndvGX'])[5]")
    GUST_DROPDOWN=(By.XPATH,"(//div[@class='sc-qnejpk-11 kgudfR'])[2]")
    NUMBER_OF_PERSONS=(By.XPATH,"(//div[@class='sc-10vdmo9-4 hndvGX'])[3]")
    DINNER_DROPDOWN=(By.XPATH,"(//div[@class='sc-qnejpk-11 kgudfR'])[3]")
    SELECT_LUNCH=(By.XPATH,"(//div[@class='sc-qnejpk-11 kgudfR'])[3]")
    SELECT_SLOT=(By.XPATH,"(//div[@class='sc-bFADNz hUuLZX'])[3]")
    CHOOSE_OFFER=(By.XPATH,"//div[@class='sc-bFADNz lmguRz']")
    CART=(By.XPATH,"(//button[@class='sc-1kx5g6g-1 cTRhrB'])[1]")


    





    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)

    def open_site(self):
        self.driver.get("https://www.zomato.com/bangalore/dine-out-in-kengeri")

      


    def click_on_spot(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 100);")
            self.wait.until(EC.element_to_be_clickable(self.CLICK_TREND_SPOT)).click()
        except Exception as e:
            print(f"Error in a click_on_spot: {e}")


    def enter_location(self,location):
        try:
            location_field = self.wait.until(EC.element_to_be_clickable(self.ENTER_LOCATION))
            location_field.send_keys(location)
            location_field.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error in a enter_location: {e}")
    
    def enter_spot_name(self,spotname):
        try:
            self.wait.until(EC.element_to_be_clickable(self.ENTER_PLACE_NAME)).send_keys(spotname)
            sleep(3)
            self.wait.until(EC.element_to_be_clickable(self.ENTER_PLACE_NAME)).click()
        except Exception as e:
            print(f"Error in a enter_spot_name: {e}")


    def click_button(self):
        try:
           
            self.wait.until(EC.element_to_be_clickable(self.CLICK_ON_SPOT)).click()
        except Exception as e:
            print(f"Error in a click_button: {e}")  


    def book_table(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.BOOK_TABLE)).click()
        except Exception as e:
            print(f"Error in book_table: {e}")

    def click_date_dropdown(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.DATE_DROPDOWN)).click()
            sleep(3)
            self.wait.until(EC.element_to_be_clickable(self.BOOKING_DATE)).click()
        except Exception as e:
            print(f"Error in click_date_dropdown: {e}")

    def click_gust_dropdown(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.GUST_DROPDOWN)).click()
            sleep(3)
            self.wait.until(EC.element_to_be_clickable(self.NUMBER_OF_PERSONS)).click()
        except Exception as e:
            print(f"Error in click_gust_dropdown: {e}")

         

    def click_dinner_dropdown(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.DINNER_DROPDOWN)).click()
            sleep(3)
            self.wait.until(EC.element_to_be_clickable(self.SELECT_LUNCH)).click()
        except Exception as e:
            print(f"Error in click_dinner_dropdown: {e}")

    def select_slot(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SELECT_SLOT)).click()
        except Exception as e:
            print(f"Error in select_slot: {e}")

    def choose_offer(self):
        try:
            self.driver.execute_script("window.scrollBy(0, 500);")
            sleep(5)
            self.wait.until(EC.element_to_be_clickable(self.CHOOSE_OFFER)).send_keys(Keys.ENTER)
            sleep(5)
        except Exception as e:
            print(f"Error in choose_offer: {repr(e)}")

    def click_cart(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CART)).click()
        except Exception as e:
            print(f"Error in click_cart: {e}")



   

                          





        

        
