from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class Searchresto:
    SEARCH_BY_PLACE=(By.XPATH,"//input[@class='sc-boCWhm gqCoZG']")
    SEARCH_HOTEL=(By.XPATH,"(//input[@placeholder='Search for restaurant, cuisine or a dish'])[1]")
    SELECT_HOTEL=(By.XPATH,"(//div[@class='sc-1q7bklc-5 kHxpSk'])[1]")
    




    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)
        

    def open_site(self):
        self.driver.get("https://www.zomato.com/bangalore/restaurants") 


    def select_location(self,location):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SEARCH_BY_PLACE)).send_keys(location)
            self.wait.until(EC.element_to_be_clickable(self.SEARCH_BY_PLACE)).send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error in a select_location: {e}")

    def search_hotel(self,name):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_HOTEL)).send_keys(name)
            self.wait.until(EC.element_to_be_clickable(self.SEARCH_HOTEL)).send_keys(Keys.ENTER)       
        except Exception as e:
            print(f"Error in a search_hotel: {e}") 

    def select_hotel(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SELECT_HOTEL)).click()
        except Exception as e:
            print(f"Error in select_hotel: {e}")


            