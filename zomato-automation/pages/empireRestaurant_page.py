from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


class EmpireRestaurantPage:
     CLICK_DILIVERY_BUTTON = (By.XPATH, "(//div[.='Delivery'])[1]")
     CLICK_EMPIRE_RESTAURANT = (By.XPATH, "//img[@alt='Empire Restaurant - Since 1966']")
     REVIEW_BUTTON = (By.XPATH, "//div[@class='sc-dmXgXv sc-hzkpqV jzMbVc']")
     PHONE_NUMBER = (By.XPATH, "//a[.='+917026610096']")

     def __init__(self,driver):
                self.driver=driver
                self.wait=WebDriverWait(self.driver,15)

     def open_site(self):
                self.driver.get("https://www.zomato.com/bangalore/restaurants?category=1")
                try:
                    self.wait.until(EC.element_to_be_clickable(self.CLICK_DILIVERY_BUTTON)).click()
                except Exception as e:
                    print(f"Error in open_site: {e}")

     def click_on_empire_restaurant(self):
                try:
                    self.driver.execute_script("window.scrollBy(0, 500);")
                    sleep(3)
                    self.wait.until(EC.element_to_be_clickable(self.CLICK_EMPIRE_RESTAURANT)).click()
                except Exception as e:
                    print(f"Error in click_on_empire_restaurant: {e}") 


     def click_review_button(self):
                try:
                    self.wait.until(EC.element_to_be_clickable(self.REVIEW_BUTTON)).click()
                except Exception as e:
                    print(f"Error in click_review_button: {e}")  
     def click_phone_number(self):
                try:
                    self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER)).click()
                except Exception as e:
                    print(f"Error in click_phone_number: {e}")  
     def alter_box(self):
                try:
                    self.driver.switch_to.alert.accept()
                except Exception as e:
                    print(f"Error in alter_box: {e}")               
