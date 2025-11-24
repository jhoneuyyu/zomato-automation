from pages.empireRestaurant_page import EmpireRestaurantPage
from time import sleep

def test_empire_restaurant(driver):
    empire_restaurant = EmpireRestaurantPage(driver)
    empire_restaurant.open_site()
    empire_restaurant.click_on_empire_restaurant()
    empire_restaurant.click_phone_number()
    sleep(5)
    empire_restaurant.alter_box()
