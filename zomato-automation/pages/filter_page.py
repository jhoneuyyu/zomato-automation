from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FilterPage:
    FILTERS=(By.XPATH,"(//div[@class='sc-jhaWeW bWqDUj pill_undefined'])[1]")
    SORT_BY=(By.XPATH,"(//p[normalize-space()='Sort by'])[1]")
    RATEING=(By.XPATH,"(//*[name()='circle'][@value='rating_desc'])[1]")
    APPLY_BTN=(By.XPATH,"(//span[@class='sc-1kx5g6g-2 iVBbNT'])[1]")
    DINNING_OUT=(By.XPATH,"(//div[contains(text(),'Dining Out')])[1]")
    CUISINES=(By.XPATH,"(//p[normalize-space()='Cuisines'])[1]")
    SEARCH_CUISINES=(By.XPATH,"(//input[@type='text'])[1]")
    NORTH_INDIAN=(By.XPATH,"(//input[@type='checkbox'])[3]")
    CLICK_CUISINES=(By.XPATH,"(//span[@class='sc-1kx5g6g-2 iVBbNT'])[1]")
    RATING_ONE=(By.XPATH,"(//p[normalize-space()='Rating'])[1]")
    



    

   



    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,15)

    def _open_site(self):
        self.driver.get("https://www.zomato.com/bangalore/restaurants?category=1")    

    def click_on_filter(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.FILTERS)).click()
        except Exception as e:
            print(f"Error in a click filter: {e}")

    def click_on_sort(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SORT_BY)).click()
        except Exception as e:
            print(f"Error in a click_on_sort: {e}")   

    def high_to_low(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.RATEING)).click()
        except Exception as e:
            print(f"Error in a high_to_low: {e}")  


    def click_on_apply(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.APPLY_BTN)).click()
        except Exception as e:
            print(f"Error in a click_on_apply: {e}")  

    def click_on_dining(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.DINNING_OUT)).click()
        except Exception as e:
            print(f"Error in a click_on_dining: {e}") 

    def click_on_cuisis(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CUISINES)).click()
        except Exception as e:
            print(f"Error in a click_on_cuisis: {e}")  

    def input_cuisines(self,text):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_CUISINES)).send_keys(text)
        except Exception as e:
            print(f"Error in a input_cuisines : {e}") 

    def click_on_north_indian(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.NORTH_INDIAN)).click()
        except Exception as e:
            print(f"Error in a click_on_north_indian: {e}") 

    def cuisines_filter_click(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CLICK_CUISINES)).click()
        except Exception as e:
            print(f"Error in a cuisines_filter_click: {e}")  

    def click_on_rating(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.RATING_ONE)).click()
        except Exception as e:
            print(f"Error in a click_on_rating: {e}")                            
    
                      

                




                              


                        








        